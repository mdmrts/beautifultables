"""Function to write CSV"""
import pandas as pd
from calc.calculations.addition import Addition
from calc.calculations.division import Division
from calc.calculations.multiplication import Multiplication
from calc.calculations.subtraction import Subtraction
import time
from datetime import datetime

now = int(time.time())
dt = datetime.fromtimestamp(now)


def writecsv(df_from_read, operation, filepath):
    df = pd.DataFrame(columns=['value_1', 'value_2', 'result', 'operation performed', 'UNIX Timestamp', 'file path'])

    if operation == "addition":
        for index, row in df_from_read.iterrows():
            mynumbers = (row['value_1'], row['value_2'])
            addition = Addition(mynumbers)
            df = df.append({'value_1': row['value_1'],
                            'value_2': row['value_2'],
                            'result': addition.get_result(),
                            'operation performed': operation,
                            'UNIX Timestamp': dt,
                            'file path': filepath},
                           ignore_index=True)

    if operation == "division":
        for index, row in df_from_read.iterrows():
            mynumbers = (row['value_1'], row['value_2'])
            division = Division(mynumbers)
            df = df.append({'value_1': row['value_1'],
                            'value_2': row['value_2'],
                            'result': division.get_result(),
                            'operation performed': operation,
                            'UNIX Timestamp': dt,
                            'file path': filepath},
                           ignore_index=True)

    if operation == "multiplication":
        for index, row in df_from_read.iterrows():
            mynumbers = (row['value_1'], row['value_2'])
            multiplication = Multiplication(mynumbers)
            df = df.append({'value_1': row['value_1'],
                            'value_2': row['value_2'],
                            'result': multiplication.get_result(),
                            'operation performed': operation,
                            'UNIX Timestamp': dt,
                            'file path': filepath},
                           ignore_index=True)

    if operation == "subtraction":
        for index, row in df_from_read.iterrows():
            mynumbers = (row['value_1'], row['value_2'])
            subtraction = Subtraction(mynumbers)
            df = df.append({'value_1': row['value_1'],
                            'value_2': row['value_2'],
                            'result': subtraction.get_result(),
                            'operation performed': operation,
                            'UNIX Timestamp': dt,
                            'file path': filepath},
                           ignore_index=True)

    df.to_csv('output1.csv', mode='a', index=False, header=False)
    print(df)
