from backend.HedgingEngine.MarkatDataReader.GenericHistory import GenericHistory
from backend.HedgingEngine.MarkatDataReader.InterestRateList import InterestRateList
from backend.HedgingEngine.MarkatDataReader.EnumCurrency import EnumCurrency





class InterestRateHistory(GenericHistory[InterestRateList]):
    """
    A specialized class to manage historical interest rates.
    """

    def get_all_rate_by_curr_name(self , curr_name : EnumCurrency) :

        list_rate = []

        for date in self.records.keys() :

            list_rate.append(self.records[date].get_rate_by_curr_name(curr_name))

        return list_rate