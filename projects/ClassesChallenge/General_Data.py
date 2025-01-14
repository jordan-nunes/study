from datetime import datetime
import pandas as pd
import numpy as np

class General_Data:
    """
    Generic class that contains all data and their respective types

    Attributes
        customer_id (str): Unique customer ID
        customer_zip_code_prefix (int): Customer ZIP code
        customer_city (str): Customer city
        customer_state (str): Customer state
        order_id (str): Unique order ID
        order_purchase_timestamp (datetime): Order timestamp (YY/MM/DD HH:MM:SS)
        order_approved_at (datetime): Order approval timestamp (YY/MM/DD HH:MM:SS)
        product_id (str): Unique product ID
        product_category_name (str): Product category
        product_weight_g (float): Product weight in grams (g)
        product_length_cm (float): Product length in centimeters (cm)
        product_height_cm (float): Product height in centimeters (cm)
        product_width_cm (float): Product width in centimeters (cm)
    """

    def __init__(self, customer_id=str, customer_zip_code_prefix=int, customer_city=str, customer_state=str, order_id=str, order_purchase_timestamp=datetime, order_approved_at=datetime, product_id=str, product_category_name=str, product_weight_g=float, product_length_cm=float, product_height_cm=float, product_width_cm=float):
        self.customer_id = customer_id
        self.customer_zip_code_prefix = customer_zip_code_prefix
        self.customer_city = customer_city
        self.customer_state = customer_state
        self.order_id = order_id
        self.order_purchase_timestamp = order_purchase_timestamp
        self.order_approved_at = order_approved_at
        self.product_id = product_id
        self.product_category_name = product_category_name
        self.product_weight_g = product_weight_g
        self.product_length_cm = product_length_cm
        self.product_height_cm = product_height_cm
        self.product_width_cm = product_width_cm

    def data_to_dict(self):
        """
        Converts the instance attributes into a dictionary.

        This method iterates through all public attributes of the instance that are not methods and 
        adds them to a dictionary if they are of type `int`, `str`, `float`, or `datetime`. 
        Private attributes and methods are ignored.

        Returns
        -------
        dict
            A dictionary containing the instance attributes as keys and their respective values, 
            limited to simple types (`int`, `str`, `float`, `datetime`).
        """
        data_dict = {}
        for attribute in dir(self):
            if not attribute.startswith('_') and not callable(getattr(self, attribute)):
                value = getattr(self, attribute)
                if isinstance(value, (int, str, float, datetime)):
                        data_dict.update({attribute: value})
        return data_dict
    
    def filter_value(key):
        int_values = ['customer_zip_code_prefix']
        datetime_values = ['order_purchase_timestamp', 'order_approved_at']
        float_values = ['product_weight_g', 'product_length_cm', 'product_height_cm', 'product_width_cm']
        if key in int_values:
            return int(0)
        elif key in datetime_values:
            default_date = datetime(2000, 1, 1, 0, 0, 0)
            return default_date.strftime('%Y-%m-%d %H:%M:%S')
        elif key in float_values:
            return 0.0
        else:
            return ''
    
    def replace_column_value(row):
        for column, value in row.items():
            if (
                value is None or
                value == '' or
                (isinstance(value, list) and len(value) == 0) or
                (isinstance(value, dict) and len(value) == 0) or
                (isinstance(value, np.ndarray) and value.size == 0) or
                value == 0 or
                value is False or
                (isinstance(value, float) and pd.isna(value))
            ):
                replacement = General_Data.filter_value(column)
                row.loc[column] = replacement
                return row
            else:
                continue
        return row