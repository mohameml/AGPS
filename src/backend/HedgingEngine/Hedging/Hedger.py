from datetime import datetime
from backend.HedgingEngine.FinancialParam.FinancialParams import FinancialParams
from backend.HedgingEngine.MarkatDataReader.EnumCurrency import EnumCurrency
from backend.HedgingEngine.Pricer.PricerGrpc import PricerGrpc
from backend.HedgingEngine.Pricer.PricingParams import PricingParams
from backend.HedgingEngine.Utils.MathDateConverter import MathDateConverter
from backend.HedgingEngine.Portfolio.Portfolio import Portfolio
from backend.HedgingEngine.MarkatDataReader.OutputData import OutputData
from backend.HedgingEngine.FinancialParam.ListDataFeed import ListDataFeed
from backend.HedgingEngine.Portfolio.PortfolioData import PortfolioData


class Hedging:

    def __init__(self, parameters: FinancialParams):

        self.financial_param = parameters
        self.marketDataReader = self.financial_param.marketDataReader
        self.converter = None  
        self.pricer = PricerGrpc(parameters)
        self.past = ListDataFeed(self.financial_param)
        # TODO : we must use the current rate
        self.r =  self.financial_param.assetDescription.get_rate_of_domesitc_currency() 
        self.dict_rf = self.financial_param.assetDescription.get_dict_interset_rate_estimate()


    def hedge(self, rebalancingDate: datetime, portfolioData: PortfolioData):

        # Récupérer les données de marché
        feed = self.get_market_data(rebalancingDate)
        
        # Mettre à jour les paramètres financiers
        self.update_financial_parameters(rebalancingDate)
        
        # Calcul des paramètres de pricing
        pricer_params = self.get_pricing_params(rebalancingDate)
        # print(pricer_params.time)
        # Calcul du pricing et des deltas
        results = self.get_price_and_deltas(pricer_params)
        
        # Création et mise à jour du portfolio
        portfolio = self.create_or_update_portfolio(results, feed, portfolioData)
        
        # Création de l'output
        output = self.create_output(results, feed.date ,portfolio.value)
        
        return output, portfolio

    def get_market_data(self, rebalancingDate: datetime):

        feed = self.marketDataReader.get_data_feed(rebalancingDate)
        if feed is None:
            raise ValueError(f"La date {rebalancingDate} n'est pas dans la période d'analyse.")
        return feed

    def update_financial_parameters(self, rebalancingDate: datetime):
        
        # Mettre à jour nombreOfDaysInOneYear
        self.financial_param.set_nb_days_in_one_year(rebalancingDate.year)
        self.converter = MathDateConverter(
            self.financial_param.nombreOfDaysInOneYear, 
            self.financial_param.time_grid.creationDate
        )


    def get_pricing_params(self, rebalancingDate: datetime):
        
        # Récupérer les informations nécessaires pour le pricing
        time_math = self.converter.ConvertToMathDistance(rebalancingDate)
        monitoring_date = rebalancingDate in self.financial_param.time_grid.paymentDates
        dict_interest_rate = self.marketDataReader.get_current_rate_dict(rebalancingDate)

        for curr in dict_interest_rate.keys() :
            if curr != EnumCurrency.EUR :
                self.dict_rf[curr] = dict_interest_rate[curr]
        # self.dict_rf = dict_interest_rate
        self.r = self.dict_rf[EnumCurrency.EUR]
        self.past.update_hedging_past(rebalancingDate)
        return PricingParams(self.past, time_math, monitoring_date , dict_interest_rate)

    
    def get_price_and_deltas(self, pricer_params):
        
        return self.pricer.price_and_deltas(pricer_params)

    def create_or_update_portfolio(self, results, feed, portfolioData):
    
        # Si c'est la première fois, on crée un portfolio avec les deltas et le prix
        portfolio = Portfolio(
            results.deltas, 
            feed.get_spot_list(self.dict_rf , self.converter),
            feed.date,  
            results.price    
        )
        
        if not portfolioData.isFirstTime:
            portfolio.set_parms(portfolioData.compos, portfolioData.cash, portfolioData.date)
            time = self.converter.ConvertToMathDistance(feed.date, portfolio.date)
            spot = feed.get_spot_list(self.dict_rf , self.converter)
            portfolio.update_compo(results.deltas, spot, feed.date, time , self.r)
        
        return portfolio

    def create_output(self, results, date, price):

        return OutputData(
            value=price , # portfolio.value if not portfolioData.isFirstTime else results.price
            date=date,
            price=results.price,
            price_std_dev=results.price_std_dev,
            deltas=list(results.deltas.values()),
            deltas_std_dev=list(results.deltas_std_dev.values())
        )

