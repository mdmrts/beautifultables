"""Division Class"""
from calc.calculations.calculation import Calculation


class Division(Calculation):
    """calculation division class"""

    def get_result(self):
        """get division results"""
        division_of_values = 1.0
        for value in self.values:
            division_of_values = value / division_of_values
        return division_of_values
