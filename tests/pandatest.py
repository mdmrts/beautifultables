"""Testing File for CSV Functionality"""
import pandas as pd
from calc.calculations.addition import Addition
from tests.readcsv import Read
from tests.absolute import absolutepath
from tests.determine_operation import Operation


addition_file = "input_test_data/addition.csv"
division_file = "input_test_data/division.csv"
multiplication_file = "input_test_data/multiplication.csv"
subtraction_file = "input_test_data/subtraction.csv"

print("Performing Addition ...")
Read.readcsv( absolutepath(addition_file), Operation.determine_operation(addition_file) )

print("Performing Division ...")
Read.readcsv( absolutepath(division_file), Operation.determine_operation(division_file) )

print("Performing Multiplication ...")
Read.readcsv( absolutepath(division_file), Operation.determine_operation(multiplication_file) )

print("Performing Subtraction ...")
Read.readcsv( absolutepath(subtraction_file), Operation.determine_operation(subtraction_file) )