"""Testing Subtraction Functionality"""
import pandas as pd

from calc.calculations.subtraction import Subtraction

from tests.absolute import absolutepath

# pylint: disable=unused-variable

def test_calculation_subtraction():
    """testing subtraction"""
    mynumbers = (2.0,6.0)
    subtraction = Subtraction(mynumbers)
    assert subtraction.get_result() == 4.0

def test_calculation_subtraction_csv():
    """testing addition"""
    file = pd.read_csv(absolutepath('input_test_data/subtraction.csv'))
    for index, row in file.iterrows():
        #Arrange
        mynumbers = (row['value_1'], row['value_2'])
        #Act
        subtraction = Subtraction(mynumbers)
        # Assert
        assert subtraction.get_result() == row['result']
