from backend.HedgingEngine.FinancialParam.FinancialParams import FinancialParams
from backend.HedgingEngine.Pricer.PricerGrpc import PricerGrpc
from backend.HedgingEngine.Pricer.PricingParams import PricingParams
from backend.HedgingEngine.Pricer.PricingResults import PricingResults
from backend.HedgingEngine.FinancialParam.DataFeed import DataFeed
from backend.HedgingEngine.Rebalacing.FixedRebalacing import FixedRebalancing
from backend.HedgingEngine.Utils.MathDateConverter import MathDateConverter
from backend.HedgingEngine.Portfolio.Portfolio import Portfolio
from backend.HedgingEngine.MarkatDataReader.OutputData import OutputData

class Hedging:
    def __init__(self, parameters: FinancialParams):

        self.financial_param = parameters
        self.pricer = PricerGrpc(parameters)
        self.oracle_rebalancing = FixedRebalancing(3) # TODO : get periode for rebalacingOrcale 

    def hedge(self, data_feeds: list[DataFeed]) -> list[OutputData]:


        converter = MathDateConverter(self.financial_param.nombreOfDaysInOneYear)
        past = [data_feeds[0]]
        monitoring_date = False
        time_math = converter.ConvertToMathDistance(
            self.financial_param.formuleDescription.creationDate, data_feeds[0].date
        )

        pricer_params = PricingParams(past, time_math, monitoring_date)
        
        results = self.pricer.price_and_deltas(pricer_params)
        
        portfolio = Portfolio(results.deltas, data_feeds[0], results.price)

        output0 = OutputData(
            value=results.price,
            date=data_feeds[0].date,
            price=results.price,
            price_std_dev=results.price_std_dev,
            deltas=list(results.deltas.values()),
            deltas_std_dev=list(results.deltas_std_dev.values())
        )

        list_output = [output0]
        
        hedging_past = [data_feeds[0]]
        
        r = self.financial_param.asset_description.currency_rates[
            self.financial_param.asset_description.domestic_currency_id
        ]

        for feed in data_feeds[1:]:
            time_math = converter.convert_to_math_distance(
                self.financial_param.payoff_description.creation_date, feed.date
            )
            monitoring_date = feed.date in self.financial_param.payoff_description.payment_dates

            if monitoring_date:
                hedging_past.append(feed)
                past = hedging_past.copy()
            else:
                past = hedging_past.copy()
                past.append(feed)

            pricer_params.set_params(past, time_math, monitoring_date)
            results = self.pricer.price_and_deltas(pricer_params)

            if self.oracle_rebalancing.is_rebalancing(feed.date):
                time = converter.convert_to_math_distance(portfolio.date, feed.date)
                value = portfolio.get_portfolio_value(feed, time, r)
                portfolio.update_compo(results.deltas, feed, value)

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