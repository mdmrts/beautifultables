"""Testing the Calculator"""
import pytest
from calc.calculator import Calculator
from calc.history.calculations import Calculations


# pylint: disable=redefined-outer-name
# pylint: disable=unused-argument

@pytest.fixture
def clear_history_fixture():
    """Clearing the history [] before each test"""
    Calculations.clear_history()


def test_calculator_add_static(clear_history_fixture):
    """Addition Test"""
    inputted_tuple = (1.0, 1.0, 6.0)
    Calculator.addition(inputted_tuple)
    assert Calculations.get_last_calculation_actual_value() == 7.0


def test_calculator_subtract_static(clear_history_fixture):
    """Subtraction Static Test"""
    inputted_tuple = (19.0, 5.0, 4.0)
    Calculator.subtraction(inputted_tuple)
    assert Calculations.get_last_calculation_actual_value() == 18.0


def test_calculator_multiply_static(clear_history_fixture):
    """Multiplication Static Test"""
    inputted_tuple = (30.0, 1.0, 2.0)
    Calculator.multiplication(inputted_tuple)
    assert Calculations.get_last_calculation_actual_value() == 60.0


def test_calculator_divide_static(clear_history_fixture):
    """Divide Static Test"""
    inputted_tuple = (5.0, 10.0)
    Calculator.division(inputted_tuple)
    assert Calculations.get_last_calculation_actual_value() == 2.0

#fullpath = path+'/'+filenamae -> test/testdata/the actual file to read/write
#in controller method, write each operation into a df and then to a csv file. Then you read that file and put it into a table which is then added to the caclulator1.html
#in the history, add values to csv in addition to adding to history