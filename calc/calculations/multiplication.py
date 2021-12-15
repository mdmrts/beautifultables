"""Multiplication Class"""
from calc.calculations.calculation import Calculation


class Multiplication(Calculation):
    """calculation multiplication class"""

    def get_result(self):
        """get multiplication results"""
        multiplication_of_values = 1.0
        for value in self.values:
            multiplication_of_values = multiplication_of_values * value
        return multiplication_of_values
