"""Testing the Addition Functionality"""
import pandas as pd

from calc.calculations.addition import Addition

from tests.absolute import absolutepath
# pylint: disable=unused-variable

def test_calculation_addition():
    """testing addition"""
    # Arrange
    mynumbers = (2.0, 3.0, 10.5)
    # Act
    addition = Addition(mynumbers)
    # Assert
    assert addition.get_result() == 15.5


def test_calculation_addition_csv():
    """testing addition"""
    file = pd.read_csv(absolutepath('input_test_data/addition.csv'))
    for index, row in file.iterrows():
        # Arrange
        mynumbers = (row['value_1'], row['value_2'])
        # Act
        addition = Addition(mynumbers)
        # Assert
        assert addition.get_result() == row['result']
