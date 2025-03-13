    
    # def hedge(self , rebalacingDate : datetime , portfolioData : PortfolioData):

    #     # params : 
    #     feed = self.marketDataReader.get_data_feed(rebalacingDate)
    #     if feed is None:
    #         raise ValueError(f"La date {rebalacingDate} n'est pas dans la période d'analyse.")
        
    #     # set nombreOfDaysInOneYear :
    #     self.financial_param.set_nb_days_in_one_year(rebalacingDate.year)
    #     self.converter = MathDateConverter(self.financial_param.nombreOfDaysInOneYear , self.financial_param.time_grid.creationDate)
        
    #     # r & r_f : 
    #     r = self.financial_param.assetDescription.get_rate_of_domesitc_currency() 
    #     dict_rf = self.financial_param.assetDescription.get_dict_interset_rate_estimate()
        

    #     # PricingParams : 
    #     time_math = self.converter.ConvertToMathDistance(rebalacingDate)
    #     monitoring_date = rebalacingDate in self.financial_param.time_grid.paymentDates
    #     # past = self.get_hedging_past(rebalacingDate)    
    #     self.past.update_hedging_past(rebalacingDate)
    #     pricer_params = PricingParams(self.past, time_math, monitoring_date)

    #     # price_and_deltas : 
    #     results = self.pricer.price_and_deltas(pricer_params)
    
    #     portfolio = Portfolio(
    #         results.deltas, 
    #         feed.get_spot_list(dict_rf),
    #         feed.date ,  
    #         results.price    
    #     )
    

    #     if portfolioData.isFirstTime :

    #         output = OutputData(
    #             value=results.price,
    #             date=feed.date,
    #             price=results.price,
    #             price_std_dev=results.price_std_dev,
    #             deltas=list(results.deltas.values()),
    #             deltas_std_dev=list(results.deltas_std_dev.values())
    #         )

    #         return output , portfolio

            
        
    #     portfolio.set_parms(portfolioData.compos , portfolioData.cash , portfolioData.date)
    #     time = self.converter.ConvertToMathDistance(feed.date , portfolio.date)
    #     value = portfolio.get_portfolio_value(feed.get_spot_list(dict_rf), time, r)
    #     portfolio.update_compo(results.deltas,feed.get_spot_list(dict_rf) , feed.date, value)

    #     # output : 

    #     output = OutputData(
    #         value=value,
    #         date=feed.date,
    #         price=results.price,
    #         price_std_dev=results.price_std_dev,
    #         deltas=list(results.deltas.values()),
    #         deltas_std_dev=list(results.deltas_std_dev.values())
    #     )

    #     return output , portfolio
        


    # def hedge(self, data_feeds: list[DataFeed]) -> list[OutputData]:

    #     # params : 
    #     r = self.financial_param.assetDescription.currencies[0].rate # self.financial_param.assetDescription.domesticCurrencyId -> 0 # TODO : a changer
    #     dict_rf = self.financial_param.assetDescription.get_dict_interset_rate_estimate()
        
        
    #     past = ListDataFeed(self.financial_param)
    #     past.addDataFeed(data_feeds[0])
    #     monitoring_date = False
    #     time_math = self.converter.ConvertToMathDistance(self.t0, data_feeds[0].date)
    #     pricer_params = PricingParams(past, time_math, monitoring_date)
        
    #     results = self.pricer.price_and_deltas(pricer_params)
    #     portfolio = Portfolio(
    #         results.deltas, 
    #         data_feeds[0].get_spot_list(dict_rf),
    #         data_feeds[0].date ,  
    #         results.price
    #     )

    #     output0 = OutputData(
    #         value=results.price,
    #         date=data_feeds[0].date,
    #         price=results.price,
    #         price_std_dev=results.price_std_dev,
    #         deltas=list(results.deltas.values()),
    #         deltas_std_dev=list(results.deltas_std_dev.values())
    #     )
    #     list_output = [output0]
    #     hedging_past = ListDataFeed(self.financial_param)
    #     hedging_past.addDataFeed(data_feeds[0])
        

    #     for feed in data_feeds[1:]:

    #         time_math = self.converter.ConvertToMathDistance(self.t0, feed.date)
    #         monitoring_date = feed.date in self.financial_param.time_grid.paymentDates

    #         if monitoring_date:
    #             # hedging_past.append(feed)
    #             hedging_past.addDataFeed(feed)
    #             # past = hedging_past
    #             past = copy.deepcopy(hedging_past)
    #         else:
    #             # past = hedging_past.copy()
    #             # past.append(feed)
    #             past = copy.deepcopy(hedging_past)
    #             past.addDataFeed(feed)

    #         pricer_params.set_params(past, time_math, monitoring_date)
    #         results = self.pricer.price_and_deltas(pricer_params)

    #         if self.oracle_rebalancing.is_rebalancing(feed.date):
    #             time = self.converter.ConvertToMathDistance(portfolio.date, feed.date)
    #             value = portfolio.get_portfolio_value(feed.get_spot_list(dict_rf), time, r)
    #             portfolio.update_compo(results.deltas,feed.get_spot_list(dict_rf) , feed.date, value)

    #             output = OutputData(
    #                 value=value,
    #                 date=feed.date,
    #                 price=results.price,
    #                 price_std_dev=results.price_std_dev,
    #                 deltas=list(results.deltas.values()),
    #                 deltas_std_dev=list(results.deltas_std_dev.values())
    #             )
    #             list_output.append(output)
        
    #     return list_output