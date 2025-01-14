from Data import Data
from General_Data import General_Data


class Order(Data):
    """
    Class to represent the data and methods of a purchase order

    Attributes
        order_id (str): Unique order ID
        order_purchase_timestamp (datetime): Purchase timestamp (YY/MM/DD/HH:MM:SS)
        order_approved_at (datetime): Approval timestamp (YY/MM/DD/HH:MM:SS)
    """

    def __init__(self, general_data):
        self.general_data = general_data

    @property
    def order_id(self):
        return self.general_data.order_id
    
    @property
    def order_purchase_timestamp(self):
        return self.general_data.order_purchase_timestamp
    
    @property
    def order_approved_at(self):
        return self.general_data.order_approved_at

    def display_data(self):
        data_dict = General_Data.data_to_dict(self)
        for attribute, value in data_dict.items():
            print(f"{attribute}: {value}")
    
    def is_empty(self):
        data_dict = General_Data.data_to_dict(self)
        for attribute, value in data_dict.items():
            if value is None or not value:
                return False
        return True
    
    def approval_delay(self, start_time, end_time):
        """
        Calculates the delay time between submission and approval of an action.

        This method calculates the difference between two timestamps, representing the time 
        between the start and the end of an approval process.

        Parameters
        ----------
        start_time : datetime
            The start time of the process.
        end_time : datetime
            The end time or approval time of the process.

        Returns
        -------
        timedelta
            The time difference between the start time and the end time, represented as a `timedelta` object.
        """
        approval_time = end_time - start_time
        return approval_time