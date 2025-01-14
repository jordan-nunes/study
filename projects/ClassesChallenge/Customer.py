from General_Data import General_Data
from Data import Data
import requests

class Customer(Data):
    """
    Class to represent customer data and methods
    
    Attributes
        customer_id (str): Unique customer ID
        customer_zip_code_prefix (int): Customer ZIP code
        customer_city (str): Customer city
        customer_state (str): Customer state
    """

    def __init__(self, general_data):
        self.general_data = general_data

    @property
    def customer_id(self):
        return self.general_data.customer_id
    
    @property
    def customer_zip_code_prefix(self):
        return self.general_data.customer_zip_code_prefix
    
    @property
    def customer_city(self):
        return self.general_data.customer_city
    
    @property
    def customer_state(self):
        return self.general_data.customer_state

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

    def fetch_zip_code_data(self, zip_code):
        """
        Check if a ZIP code is valid.

        This method receives a ZIP code, makes a request to the ViaCEP API, and returns a dictionary 
        with the corresponding address information such as street, neighborhood, city, and state. 
        If the ZIP code is invalid or there is a request error, it returns None.

        Parameters
        ----
        zip_code : int

        Returns:
        ----
        dict or None

        A dictionary with the address data if the ZIP code is valid, or None if the ZIP code is invalid 
        or there is a request error.
        """
        url = f"https://viacep.com.br/ws/{zip_code}/json/"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if 'erro' not in data:
                return data
            else:
                return None
        else:
            return None

    def validate_city_and_state(self, zip_code, city, state):
        """
        Validates if the city and state match the provided ZIP code.

        This method uses data obtained from a ZIP code lookup to verify if the city (`localidade`) and 
        state (`uf`) match the provided parameters. The comparison is case-insensitive. If the ZIP code 
        is invalid or the lookup returns no data, the function returns False.

        Parameters
        ----------
        zip_code : str
            The ZIP code to be validated.
        city : str
            The city to compare with the locality returned by the ZIP code lookup.
        state : str
            The state (UF) to compare with the state returned by the ZIP code lookup.

        Returns
        -------
        bool
            Returns True if the city and state match the ZIP code data, or False
            (including in case of a ZIP code lookup error).
        """
        data = self.fetch_zip_code_data(zip_code)
        if data is None:
            return False
        elif str(data['localidade']).lower() == city.lower() and str(data['uf']).upper() == state.upper():            
            return True
        else:
            return False