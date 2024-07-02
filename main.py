import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import functions as func

path_file = 'files\\20240620_a1b2g2-EtOH-1h_zelle1.asc' # load file Path


# Pfad zur .asc-Datei
data_frames = func.read_multiple_measurements(path_file)

# Spaltennamen in jedem DataFrame bereinigen
for df in data_frames:
    df.columns = df.columns.str.strip()

# Überprüfen der Daten
for i, df in enumerate(data_frames):
    print(f"DataFrame {i + 1}:")
    print(df.head())
    print(df.columns)


#     # DataFrame in eine CSV-Datei speichern
# df.to_csv('dataframe_output.csv', index=False)

# # CSV-Datei öffnen (kann in einem Texteditor oder Tabellenkalkulationsprogramm geöffnet werden)
# import os
# os.startfile('dataframe_output.csv')

# Graphen erstellen
df['"Time[s]"'] = pd.to_numeric(df['"Time[s]"'], errors='coerce')
df['"I-mon[A]"'] = pd.to_numeric(df['"I-mon[A]"'], errors='coerce')

# Graph erstellen
plt.figure(figsize=(10, 6))
plt.plot(df['"Time[s]"'], df['"I-mon[A]"'], marker='x', linestyle='-')
plt.xlabel('Time [s]')
plt.ylabel('I-mon [A]')
plt.title('Messung')
plt.grid(False)
plt.show()