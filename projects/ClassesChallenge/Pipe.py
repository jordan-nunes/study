import pandas as pd

class Pipe:
    """
    Class to manipulate stack methods

    Attributes:
        data (pandas.Series): Pandas data series
    """
    
    def __init__(self, data=pd.Series):
        self.data = data
    
    def separate_lifo_data(self):
        """
        Separates the last row of data from the dataframe

        This method receives a dataframe of type pd.Series and returns the last row.

        Returns:
        ----------
        pandas.core.frame.DataFrame
            The last row of the dataframe
        """
        return self.data.iloc[-1].copy()

    def remove_data_from_dataframe(self):
        """
        This method removes the last row of data from the dataframe

        Returns:
        ----------
        pd.Series
            The dataframe without the last row
        """
        self.data = self.data.drop(self.data.index[-1])
        return self.data