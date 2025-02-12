from backend.HedgingEngine.MarkatDataReader.GenericHistory import GenericHistory
from backend.HedgingEngine.MarkatDataReader.ExchangeRateList import ExchangeRateList
from backend.HedgingEngine.MarkatDataReader.EnumCurrency import EnumCurrency



class ExchangeRateHistory(GenericHistory[ExchangeRateList]):
    """
    A specialized class to manage historical exchange rates.
    """
    
    def get_all_rate_by_currency_name(self , curr_name : EnumCurrency):
        """
            - return List[float] : X_i(t0) , ........ , X_i(t_N) avec i : curr_name
        """
        list_rate = []
        for date in self.records.keys():
            list_rate.append(self.records[date].get_rate_by_currency_name(curr_name))

        return list_rate

    def get_all_rate_for_all_curr_name(self) :
        
        """
            - return matrix M = [  X_2 , ... X_5 ]
            - avec X_i : X_i(t0) , ........ , X_i(t_N) ,  i : curr_name
        """

        matrix_rate = []

        for curr_name in EnumCurrency :

            if(curr_name != EnumCurrency.EUR) :

                list_rate = self.get_all_rate_by_currency_name(curr_name)
                matrix_rate.append(list_rate)
            
        return matrix_rate
