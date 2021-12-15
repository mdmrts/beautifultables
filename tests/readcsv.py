"""Function to read CSV"""
import pandas as pd
# from writecsv import writecsv
from tests.absolute import absolutepath

out_file = "tests/output_csv_file/output2.csv"


class Read:
    # def readcsv(filepath, operation):
    #     file = pd.read_csv(filepath)
    #     return writecsv(file, operation, filepath)

    @staticmethod
    def csvreader():
        file = pd.read_csv(absolutepath(out_file))
        return file
