"""This is the increment function"""
# facade program
from calc.history.calculations import Calculations
# pylint: disable=line-too-long

class Calculator:
    """This is the Calculator Class which calls the Calculations class to perform calculator duties"""

    @staticmethod
    def addition(values_assigned_to_tuple: tuple):
        """adds list of numbers"""
        Calculations.addition_calculation(values_assigned_to_tuple)
        return True

    @staticmethod
    def subtraction(values_assigned_to_tuple: tuple):
        """subtract list of numbers"""
        Calculations.subtraction_calculation(values_assigned_to_tuple)
        return True

    @staticmethod
    def multiplication(values_assigned_to_tuple: tuple):
        """multiplication numbers from result"""
        Calculations.multiplication_calculation(values_assigned_to_tuple)
        return True

    @staticmethod
    def division(values_assigned_to_tuple: tuple):
        """divide numbers from result"""
        Calculations.division_calculation(values_assigned_to_tuple)
        return True
