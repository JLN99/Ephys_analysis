"""
Functions for the data frame organisation
"""

# import of packages
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

def asc_to_df(file_path):
    """
    Loads a ascii-file and extracts the measured data into an data frame.
    The measurments are sorted after the time and the related I-mon at that time for each sweep/Series.
    
    Input: file path to the ascii file
    Output: structured data frame for future analysis and plotting -> time[s] I-mon sweep 1, 2, 3, etc.
    """
    # opens the ascii file and parses over every line and stores that content
    with open(file_path, "r") as file:
        content = file.readlines()

    # working variables
    series = None       # var. for the name of each series
    series_df = []      # array in which the data frames of each sweep are collected 
    series_data = []    # array storing the I-mon data of each sweep temporarly

    # Iterates over each line from the ascii file and checks wether a new series starts or if they are still data - stores data in df
    for line in content:
        # checks if the line starts with "Series", "Index" - stores Series name in vsriable 'series' 
        if line.startswith("Series_"):
            series = line.strip()
        elif line.startswith('"Index"'):        # starts with an empty df after each "Index"
            series_data = []
        elif series and line.strip():           # cehcks if a series name was set and the following colums are filled with data (stiped from all spaces)
            # Splits the column separated by ',' and stores them in col_parts without spaces
            col_parts = line.strip().split(',')
            try:
                # Checks if the data found in the column is of the correct structure -> Stores each info in separate variables
                index = int(col_parts[0])
                time_s = float(col_parts[1])
                i_mon = float(col_parts[2])
                series_data.append([index, time_s, i_mon])      # appends the array with the found data
            except ValueError:
                # If the data was not in the right format or empty the column is skipped e.g. if there is a column containing text
                continue

        elif line.strip() == '' and series:
            # After an empty column of the series -> the collected data is transfered into a data frame
            if series_data:
                # Convertes the collected data into a data frame and appends the array column by column
                df = pd.DataFrame(series_data, columns=["Index", "Time[s]", series])
                series_df.append(df)
            series = None       # sets the series name back to an empty value 

    # Merges all generated df of each sweep into one df. All values are aligned after the constant variable "Time[s]"
    if series_df:       # checks if the df is not empty
        result_df = series_df[0][["Time[s]"]]  # Sets the "Time[s]" as the first row
        for df in series_df:        # Merges all df into on -> the time data is everytime the same so its only inserted once
            result_df = result_df.merge(df[["Time[s]", df.columns[-1]]], on="Time[s]")

        return result_df        # returns the genarated df



def analyze_folder(folder_path):
    '''
    creates a loop that iterates over the folder contant and generates from all ascii files a data frame with the function asc_to_df
    '''
    result_df = {} # created an empty directory

    for file in os.listdir(folder_path):            # enumerates over the files in the folder
        file_path = os.path.join(folder_path, file) # generates the correct path to each file
        if file.endswith('.asc'):                   # if the file ends with '.asc' it gets turned into a df via asc_to_df function
            df = asc_to_df(file_path)
            file_name = os.path.splitext(file)[0]
            result_df[file_name] = df               # extends the directory with every created df
    return result_df                                # returns df


def create_plot(df_directory):
    
    for name, df in df_directory.items():
        plt.figure()
        for col in df.columns:
            if col != 'Time[s]':
                plt.plot(df['Time[s]'], df[col], label = col)
        
        plt.title(name)
        plt.xlabel('Time[s]')
        plt.ylabel('I-mon')
        plt.legend()

        plt.savefig(f"{name}.png")
        plt.show()
       
        plt.close()


# test
folder_path = "C:\\Users\\julia\\lokales-Archiv\\PhD\\Data_analysis_python\\Ephys_analysis\\ascii-files"
dfs_test = analyze_folder(folder_path)
print(dfs_test)
create_plot(dfs_test)



# # Graph erstellen
# plt.figure(figsize=(10, 6))
# #loop machen, welcher über die länge aller gespeicherten Sweeps geht und diese darstellt. Außerdem erstellung von einer Legende
# plt.plot(df['Time[s]'], df['Series_2_1'], marker='x', linestyle='-', color="black")
# plt.plot(df['Time[s]'], df['Series_2_2'], marker='x', linestyle='-')
# plt.plot(df['Time[s]'], df['Series_2_3'], marker='x', linestyle='-')
# plt.plot(df['Time[s]'], df['Series_2_4'], marker='x', linestyle='-')
# plt.plot(df['Time[s]'], df['Series_2_5'], marker='x', linestyle='-')
# plt.plot(df['Time[s]'], df['Series_2_6'], marker='x', linestyle='-')
# plt.plot(df['Time[s]'], df['Series_2_7'], marker='x', linestyle='-')
# plt.plot(df['Time[s]'], df['Series_2_8'], marker='x', linestyle='-')

# plt.xlabel('Time [s]')
# plt.ylabel('I-mon [A]')
# plt.title('Messung')
# plt.grid(False)
# plt.show()