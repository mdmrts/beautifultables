"""This class performs the basic calculator functions"""
from calc.addition import Addition
from calc.subtraction import Subtraction
from calc.multiplication import Multiplication
from calc.division import Division

class Calculator:
    """ This is the Calculator class"""

    history = []

    @staticmethod
    def clear_history():
        """Clears all values in the history"""
        Calculator.history.clear()
        return True

    @staticmethod
    def add_calculation_to_history(calculation):
        """Adds  calculation to the history"""
        Calculator.history.append(calculation)
        return True



    @staticmethod
    def get_result_of_last_calculation_added_to_history():
        """Returns the most recent value in the history"""
        return Calculator.history[-1].get_result()


    @staticmethod
    def get_result_of_first_calculation_added_to_history():
        """Returns the first result in the history"""
        return Calculator.history[0].get_result()

    @staticmethod
    def history_count():
        """Returns the number of items in the history"""
        return len(Calculator.history)

    @staticmethod
    def add_numbers(value_a, value_b):
        """adds value_a and value_b"""
        addition = Addition.create(value_a, value_b)
        Calculator.add_calculation_to_history(addition)
        return Calculator.get_result_of_last_calculation_added_to_history()

    @staticmethod
    def subtract_numbers(value_a, value_b):
        """subtracts value_b from value_a"""
        subtraction = Subtraction.create(value_a, value_b)
        Calculator.add_calculation_to_history(subtraction)
        return Calculator.get_result_of_last_calculation_added_to_history()

    @staticmethod
    def multiply_numbers(value_a, value_b):
        """multiplies value_a by value_b"""
        multiplication = Multiplication.create(value_a, value_b)
        Calculator.add_calculation_to_history(multiplication)
        return Calculator.get_result_of_last_calculation_added_to_history()

    @staticmethod
    def divide_numbers(value_a, value_b):
        """divides value_a by value_b, shows an error if value_b is 0"""
        division = Division.create(value_a, value_b)
        Calculator.add_calculation_to_history(division)
        return Calculator.get_result_of_last_calculation_added_to_history()
    @staticmethod
    def get_last_object():
        """Returns the most recent object of the calculator history"""
        return Calculator.history[-1]

    @staticmethod
    def get_history():
        """Returns the full history"""
        return Calculator.history