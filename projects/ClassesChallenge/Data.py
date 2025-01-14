from abc import ABC, abstractmethod

class Data(ABC):
    """
    Abstract base class for data coming from the database
    """

    def __init__(self):
        pass

    @abstractmethod
    def display_data(self):
        """
        Displays the public properties and values of the object.

        This method iterates through all public attributes and properties that do not start with an 
        underscore ('_') and are not methods (functions) whose value is of type int, str, float, or datetime. 
        Then, it displays the name and value of each of these attributes.
        """
        pass

    @abstractmethod
    def is_empty(self) -> bool:
        """
        Checks if all public attributes and properties of the object are populated.

        This method iterates through all public attributes and properties that do not start with an 
        underscore ('_') and are not methods (functions) whose value is of type int, str, float, or datetime. 
        Then, it returns True if all attributes are populated and False otherwise.

        Returns
        ----
        bool: True if all attributes are populated, False otherwise
        """
        pass