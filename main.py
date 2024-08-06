'''
Starting Steps: 
    1. Enter/Create the virtuall enviroment: comand: pipenv shell
    -> opens or generates virt. envirment depending on the existing pipfile. - allways the same package versions
    2. lunching python files via the shell terminal: python filename.py 
    3. after editing or new code push to github!
'''


import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

import functions as func # file contains the functions created for the ascii importation

path_file = 'ascii-files\\20240620_a1b2g2-EtOH-1h_zelle2.asc' # load file Path


# Pfad zur .asc-Datei
df = func. parse_measurements(path_file)

print(df.head())
print(df.columns)


#     # DataFrame in eine CSV-Datei speichern
# df.to_csv('dataframe_output.csv', index=False)

# # CSV-Datei öffnen (kann in einem Texteditor oder Tabellenkalkulationsprogramm geöffnet werden)
# import os
# os.startfile('dataframe_output.csv')
# Graphen erstellen
df['Time[s]'] = pd.to_numeric(df['Time[s]'], errors='coerce')
#df['I-mon[A]"'] = pd.to_numeric(df['"I-mon[A]"'], errors='coerce')

# Graph erstellen
plt.figure(figsize=(10, 6))
#loop machen, welcher über die länge aller gespeicherten Sweeps geht und diese darstellt. Außerdem erstellung von einer Legende
plt.plot(df['Time[s]'], df['Series_2_1'], marker='x', linestyle='-', color="black")
plt.plot(df['Time[s]'], df['Series_2_2'], marker='x', linestyle='-')
plt.plot(df['Time[s]'], df['Series_2_3'], marker='x', linestyle='-')
plt.plot(df['Time[s]'], df['Series_2_4'], marker='x', linestyle='-')
plt.plot(df['Time[s]'], df['Series_2_5'], marker='x', linestyle='-')
plt.plot(df['Time[s]'], df['Series_2_6'], marker='x', linestyle='-')
plt.plot(df['Time[s]'], df['Series_2_7'], marker='x', linestyle='-')
plt.plot(df['Time[s]'], df['Series_2_8'], marker='x', linestyle='-')

plt.xlabel('Time [s]')
plt.ylabel('I-mon [A]')
plt.title('Messung')
plt.grid(False)
plt.show()