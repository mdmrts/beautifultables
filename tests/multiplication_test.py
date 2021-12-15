"""Multiplication test"""
import pandas as pd

from calc.calculations.multiplication import Multiplication

from tests.absolute import absolutepath

# pylint: disable=unused-variable

def test_calculation_multiplication():
    """test multiplication"""
    mynumbers = (6.0, 5.0, 2.0)
    multiplication = Multiplication(mynumbers)
    assert multiplication.get_result() == 60.0


def test_calculation_multiplication_csv():
    """testing multiplication from imported csv"""
    file = pd.read_csv(absolutepath('input_test_data/multiplication.csv'))
    for index, row in file.iterrows():
        # Arrange
        mynumbers = (row['value_1'], row['value_2'])
        # Act
        multiplication = Multiplication(mynumbers)
        # Assert
        assert multiplication.get_result() == row['result']
