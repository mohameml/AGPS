from backend.HedgingEngine.FinancialParam.ListDataFeed import ListDataFeed
from backend.HedgingEngine.FinancialParam.FinancialParams import FinancialParams
from backend.HedgingEngine.Pricer.PricerGrpc import PricerGrpc
from backend.HedgingEngine.Pricer.PricingParams import PricingParams
from backend.HedgingEngine.Pricer.PricingResults import PricingResults
from backend.HedgingEngine.FinancialParam.DataFeed import DataFeed
from backend.HedgingEngine.Utils.MathDateConverter import MathDateConverter
from backend.HedgingEngine.Portfolio.Portfolio import Portfolio
from backend.HedgingEngine.MarkatDataReader.OutputData import OutputData
# from backend.HedgingEngine.Rebalacing.FixedRebalacing import 
from backend.HedgingEngine.Rebalacing.Rebalacing import Rebalancing
import copy
class Hedging:
    def __init__(self, parameters: FinancialParams):

        self.financial_param = parameters
        self.converter = MathDateConverter(self.financial_param.nombreOfDaysInOneYear)
        self.t0 = self.financial_param.formuleDescription.creationDate
        self.pricer = PricerGrpc(parameters)
        self.oracle_rebalancing = Rebalancing.create_rebalancing("FixedRebalancing" , 3)  #FixedRebalancing(3) # TODO : get periode for rebalacingOrcale 

    def hedge(self, data_feeds: list[DataFeed]) -> list[OutputData]:

        # params : 
        r = self.financial_param.assetDescription.currencies[0].rate # self.financial_param.assetDescription.domesticCurrencyId -> 0 # TODO : a changer
        dict_rf = self.financial_param.assetDescription.get_dict_interset_rate_estimate()
        
        
        past = ListDataFeed(self.financial_param)
        past.addDataFeed(data_feeds[0])
        monitoring_date = False
        time_math = self.converter.ConvertToMathDistance(self.t0, data_feeds[0].date)
        pricer_params = PricingParams(past, time_math, monitoring_date)
        
        results = self.pricer.price_and_deltas(pricer_params)
        portfolio = Portfolio(
            results.deltas, 
            data_feeds[0].get_spot_list(dict_rf),
            data_feeds[0].date ,  
            results.price
        )

        output0 = OutputData(
            value=results.price,
            date=data_feeds[0].date,
            price=results.price,
            price_std_dev=results.price_std_dev,
            deltas=list(results.deltas.values()),
            deltas_std_dev=list(results.deltas_std_dev.values())
        )
        list_output = [output0]
        hedging_past = ListDataFeed(self.financial_param)
        hedging_past.addDataFeed(data_feeds[0])
        

        for feed in data_feeds[1:]:

            time_math = self.converter.ConvertToMathDistance(self.t0, feed.date)
            monitoring_date = feed.date in self.financial_param.formuleDescription.paymentDates

            if monitoring_date:
                # hedging_past.append(feed)
                hedging_past.addDataFeed(feed)
                # past = hedging_past
                past = copy.deepcopy(hedging_past)
            else:
                # past = hedging_past.copy()
                # past.append(feed)
                past = copy.deepcopy(hedging_past)
                past.addDataFeed(feed)

            pricer_params.set_params(past, time_math, monitoring_date)
            results = self.pricer.price_and_deltas(pricer_params)

            if self.oracle_rebalancing.is_rebalancing(feed.date):
                time = self.converter.ConvertToMathDistance(portfolio.date, feed.date)
                value = portfolio.get_portfolio_value(feed.get_spot_list(dict_rf), time, r)
                portfolio.update_compo(results.deltas,feed.get_spot_list(dict_rf) , feed.date, value)

                output = OutputData(
                    value=value,
                    date=feed.date,
                    price=results.price,
                    price_std_dev=results.price_std_dev,
                    deltas=list(results.deltas.values()),
                    deltas_std_dev=list(results.deltas_std_dev.values())
                )
                list_output.append(output)
        
        return list_output