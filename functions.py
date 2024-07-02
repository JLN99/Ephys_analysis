"""
Functions for the data frame organisation
"""

# import of the needed functions
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



def test(name):
    print(name + "test")
    return name

def read_multiple_measurements(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    data_frames = []
    current_data = []
    header = None
    for line in lines:
        if line.startswith(':Series') or line.startswith('Sweep'):
            if current_data:
                df = pd.DataFrame(current_data[1:], columns=current_data[0])
                data_frames.append(df)
                current_data = []
        elif line.startswith('"Index"'):
            header = line.strip().split(', ')
            current_data.append(header)
        else:
            values = line.strip().split(', ')
            current_data.append(values)

    # Add the last dataset if there is any
    if current_data:
        df = pd.DataFrame(current_data[1:], columns=current_data[0])
        data_frames.append(df)

    return data_frames