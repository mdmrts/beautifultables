"""Mod Calculation Class"""

# pylint: disable=too-few-public-methods
# pylint: disable=line-too-long

class Calculation:  # Abstraction
    """calculation abstract base class"""

    def __init__(self, values: tuple):
        """constructor method (instance method) -> instances are created from this constructor"""
        self.values = Calculation.convert_args_to_tuple_float(values)  # instance attribute

    @classmethod
    def create(cls, values: tuple):
        """this is the factory method -> factory methods are useful for input types determined at runtime"""
        return cls(values)  # class attribute

    @staticmethod
    def convert_args_to_tuple_float(values):
        """convert list of arguments to floats"""
        list_values_float = []
        for value in values:
            list_values_float.append(float(value))
        return tuple(list_values_float)  # convert list to tuple
