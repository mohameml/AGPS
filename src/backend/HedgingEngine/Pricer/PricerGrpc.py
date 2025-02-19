import grpc
from backend.HedgingEngine.FinancialParam.DataFeed import DataFeed
from backend.HedgingEngine.FinancialParam.FinancialParams import FinancialParams
from backend.HedgingEngine.Pricer import pricing_pb2
from backend.HedgingEngine.Pricer import pricing_pb2_grpc
from backend.HedgingEngine.Pricer.Pricer import Pricer
from backend.HedgingEngine.Pricer.PricingParams import PricingParams

class PricerGrpc(Pricer):

    def __init__(self, financial_parameters: FinancialParams , address: str = "http://localhost:50051"):
        
        super().__init__(financial_parameters)
        self.channel = grpc.insecure_channel(address)
        self.grpc_client = pricing_pb2_grpc.GrpcPricerStub(self.channel)

    def price_and_deltas(self, pricing_params):
        input_data = self.pricing_params_to_pricing_input(pricing_params)
        output = self.grpc_client.PriceAndDeltas(input_data)


        # TODO : encapsule output dans PricingResult : 
    
        return {
            "price": output.price,
            "deltas": list(output.deltas),
            "price_std_dev": output.priceStdDev,
            "deltas_std_dev": list(output.deltasStdDev),
            "assets": list(pricing_params.data_feeds[0].spot_list.keys())
        }

    def hello_world(self):
        info = self.grpc_client.HelloWorld(pricing_pb2.Empty())
        print(f"Message reçu : {info.message}")
        return info

    # TODO : convert all PrcingParams to PricingInput (dans .proto) :

    def pricing_params_to_pricing_input(self, pricing_params : PricingParams):
        
        input_data = pricing_pb2.PricingInput()
        
        # 1) Convert ListDataFeed to pastLines un marketDomestic : past 

        for feed in pricing_params.data_feeds:
            line = pricing_pb2.PastLines()
            line.value.extend(feed.toDomesticMarket())
            input_data.past.append(line)
        
        # 2) Convert to monitoringDateReached and time : 
        input_data.monitoringDateReached = pricing_params.monitoring_date
        input_data.time = pricing_params.time
        input_data.domesticCurrencyId = self.params.assetDescription.domesticCurrencyId

        # 3) Convet params.assetDescription.currencies to Grpc.currencies : 

        for curr in self.params.assetDescription.currencies : 
            currency = pricing_pb2.Currency(id=curr.id , 
                                            interestRate=curr.rate , 
                                            volatility= curr.volatility)
            input_data.currencies.append(currency)
        
        
        # 4) Convert assets : 

        for asset in self.params.assetDescription.assets : 
            Asset = pricing_pb2.Asset(currencyId=asset.id , volatility=asset.volatility)
            input_data.assets.append(Asset);

        # 5) CorrelationMatrix : 

        for line in self.params.assetDescription.matrix_corr : 
            row = pricing_pb2.CorrelationMatrix()
            row.value.extend(line)
            input_data.correlations.append(row)

        # 6) timeGrid : 
        input_data.time_grid.value.extend(self.params.formuleDescription.time_grid)

        return input_data
