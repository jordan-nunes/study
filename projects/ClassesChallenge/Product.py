from General_Data import General_Data
from Data import Data

class Product(Data):
    """
    Class to represent the data and methods of a product

    Attributes
        product_id (str): Unique product ID
        product_category_name (str): Product category
        product_weight_g (float): Product weight in grams (g)
        product_length_cm (float): Product length in centimeters (cm)
        product_height_cm (float): Product height in centimeters (cm)
        product_width_cm (float): Product width in centimeters (cm)
    """

    def __init__(self, general_data):
        self.general_data = general_data

    @property
    def product_id(self):
        return self.general_data.product_id
    
    @property
    def product_category_name(self):
        return self.general_data.product_category_name
    
    @property
    def product_weight_g(self):
        return self.general_data.product_weight_g
    
    @property
    def product_length_cm(self):
        return self.general_data.product_length_cm
    
    @property
    def product_height_cm(self):
        return self.general_data.product_height_cm
    
    @property
    def product_width_cm(self):
        return self.general_data.product_width_cm

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
    
    def calculate_volume(self, dimension_1, dimension_2, dimension_3):
        """
        Calculates the cubic volume from three dimensions.

        This method calculates the volume of an object or space by multiplying three provided dimensions.

        Parameters
        ----------
        dimension_1 : float
            The first dimension (length).
        dimension_2 : float
            The second dimension (width).
        dimension_3 : float
            The third dimension (height).

        Returns
        -------
        float
            The resulting volume from the multiplication of the three dimensions.
        """
        return dimension_1 * dimension_2 * dimension_3