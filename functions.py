"""
Functions for the data frame organisation
"""

# import of packages
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
from scipy.integrate import simpson # Verwenden für Flächenberechnung unter der Kurve

# def asc_to_df_alt(file_path):
#     """
#     Loads a ascii-file and extracts the measured data into an data frame.
#     The measurments are sorted after the time and the related I-mon at that time for each sweep/Series.
    
#     Input: file path to the ascii file
#     Output: structured data frame for future analysis and plotting -> time[s] I-mon sweep 1, 2, 3, etc.
#     """
#     # opens the ascii file and parses over every line and stores that content
#     with open(file_path, "r") as file:
#         content = file.readlines()

#     # working variables
#     series = None       # var. for the name of each series
#     series_df = []      # array in which the data frames of each sweep are collected 
#     series_data = []    # array storing the I-mon data of each sweep temporarly

#     # Iterates over each line from the ascii file and checks wether a new series starts or if they are still data - stores data in df
#     for line in content:
#         # checks if the line starts with "Series", "Index" - stores Series name in vsriable 'series' 
#         if line.startswith("Series_"):
#             series = line.strip()
#         elif line.startswith('"Index"'):        # starts with an empty df after each "Index"
#             series_data = []
#         elif series and line.strip():           # cehcks if a series name was set and the following colums are filled with data (stiped from all spaces)
#             # Splits the column separated by ',' and stores them in col_parts without spaces
#             col_parts = line.strip().split(',')
#             try:
#                 # Checks if the data found in the column is of the correct structure -> Stores each info in separate variables
#                 index = int(col_parts[0])
#                 time_s = float(col_parts[1])
#                 i_mon = float(col_parts[2])
#                 series_data.append([index, time_s, i_mon])      # appends the array with the found data
#             except ValueError:
#                 # If the data was not in the right format or empty the column is skipped e.g. if there is a column containing text
#                 continue

#         elif line.strip() == '' and series:
#             # After an empty column of the series -> the collected data is transfered into a data frame
#             if series_data:
#                 # Convertes the collected data into a data frame and appends the array column by column
#                 df = pd.DataFrame(series_data, columns=["Index", "Time[s]", series])
#                 series_df.append(df)
#             series = None       # sets the series name back to an empty value 

#     # Merges all generated df of each sweep into one df. All values are aligned after the constant variable "Time[s]"
#     if series_df:       # checks if the df is not empty
#         result_df = series_df[0][["Time[s]"]]  # Sets the "Time[s]" as the first row
#         for df in series_df:        # Merges all df into on -> the time data is everytime the same so its only inserted once
#             result_df = result_df.merge(df[["Time[s]", df.columns[-1]]], on="Time[s]")

#         return result_df        # returns the genarated df

###################################################

# def convert_asc_to_df(file_path):
#     """
#     Loads a ascii-file and extracts the measured data into an data frame.
#     The measurments are sorted after the time and the related I-mon at that time for each sweep/Series.
#     """

def max_current_per_series(df: pd.DataFrame, r: int = 50 , timeframe_min: float = 1.1, timeframe_max: float = 5.0):
    """
    Checks each column (except the time) and creates the Mean of the 50(definable range(r) values before and after the Max Value.
    -> The Mean should make the determination more robust
    Values are only taken into account after 1.0s and 5.0s -> Should reduce 

    Input:   df that is already sorted acording to time and series 1 - X
    Output:  returns 
    """

    # reduces the df to a subset containting only the values after 1s and 5s (default -> can be set manualy)
    df_timeframe = df.query('time >= @timeframe_min & time <= @timeframe_max')

    mean_values = []
   
    

    for column in df.columns[1:]:
        
        index_maxCurrent = df_timeframe[column].idxmin()
        max_time = df_timeframe.query(f"index == {index_maxCurrent}")['time'].iloc[0]
        start_index = max(0, index_maxCurrent - r)
        end_index = min(len(df_timeframe), index_maxCurrent + r + 1)
        
        mean_IMAX = df_timeframe[column].iloc[start_index:end_index].mean()

        # schnell von chatgpt: # unbedingt noch umschreiben! ist nur für ne kurze überprüfung gewesen!
        conc = [1,2,3,4,5,6,7,8]
        mean_values.append(mean_IMAX)

        print(mean_IMAX)
        
    plt.figure(figsize=(8, 6))
    plt.plot(range(1, len(conc) + 1), mean_values, marker='o', linestyle='-', color='b')

    # Achsen und Titel hinzufügen
    plt.xlabel('Sweep Nummer')
    plt.ylabel('Durchschnittlicher Strom (IMAX)')
    plt.title('IMAX Mittelwerte pro Sweep')

    # Anzeigen des Plots
    plt.xticks(range(1, len(conc) + 1))
    plt.grid(True)
    plt.show()
    # print(df_timeframe.head())













def asc_to_df(file_path: str):
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
                #print(f"!!!Zeile konnte nicht konvertiert werden: {line}") # advisable to use it for checking the first time a set of
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
        result_df.rename(columns={"Time[s]": "time"}, inplace=True)
        return result_df        # returns the genarated df

########################################################################




def analyze_folder(folder_path: str):
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


#test
# file_path = 'ascii-files' #\\20240620_a1b2g2-EtOH-1h_zelle2.asc'
# df = analyze_folder(file_path)
# comb_df = pd.concat(df, names=['Measurment'])
# comb_df.to_csv('testdf.csv', index=False)
# print(comb_df)

def create_plot(df_directory: pd.DataFrame):
    
    for name, df in df_directory.items():
        plt.figure()
        for col in df.columns:
            if col != 'Time[s]':
                plt.plot(df['Time[s]'], df[col], label = col)
        
        plt.title(name)
        plt.xlabel('Time[s]')
        plt.ylabel('I-mon')
        plt.legend()
        plt.xticks(range(0, 11, 1)) # sets the tickrate to 1 from 1-10
        plt.savefig(f"{name}.png")
        plt.show()
       
        plt.close()

def create_plot_area_under_trace(df_directory: pd.DataFrame): # von chatgpt unbedingt überarbeiten -> Area under the curve funktioniert noch nicht zu berechnen!
    num_traces = sum(len(df.columns) - 1 for df in df_directory.values())  # Anzahl der Plots (jede Spalte außer 'Time[s]')
    cols = 3  # Anzahl der Spalten in der Collage
    rows = int(np.ceil(num_traces / cols))  # Anzahl der Reihen
    
    fig, axes = plt.subplots(rows, cols, figsize=(15, 10))
    axes = axes.flatten()  # Damit wir die Achsen im Raster leichter ansprechen können
    
    plot_index = 0  # Zähler für den aktuellen Subplot
    
    for name, df in df_directory.items():
        for col in df.columns:
            if col != 'Time[s]':
                time = df['Time[s]']
                trace = df[col]
                
                # Null-Linie definieren (der Anfangswert der Messung)
                baseline = trace.iloc[0]
                
                # Wähle das aktuelle Achsen-Objekt
                ax = axes[plot_index]
                
                # Plot der Trace
                ax.plot(time, trace, label=col)
                
                # Berechne die Fläche unter der Kurve (relativ zum Anfangswert)
                area = simpson(trace - baseline, x=time)
                
                # Färbe die Fläche unter der Kurve (zwischen baseline und trace)
                ax.fill_between(time, trace, baseline, alpha=0.3)
                
                # Zeige die berechnete Fläche im Plot an
                ax.text(0.05, 0.95, f'Area: {area:.2f}', transform=ax.transAxes, 
                        verticalalignment='top', bbox=dict(facecolor='white', alpha=0.5))
                
                # Setze Titel, Achsenbeschriftung und Legende
                ax.set_title(f'{name} - {col}')
                ax.set_xlabel('Time[s]')
                ax.set_ylabel('I-mon')
                ax.legend()
                ax.set_xticks(range(0, 11, 1))  # Setzt die Tickrate von 1-10
                
                # Zum nächsten Subplot weitergehen
                plot_index += 1
    
    # Entferne ungenutzte Subplots (falls weniger als 9 Plots vorhanden sind)
    for j in range(plot_index, len(axes)):
        fig.delaxes(axes[j])
    
    plt.tight_layout()
    plt.savefig(f"all_traces_collage.png")
    plt.show()

    plt.close()

