"""
Functions for the data frame organisation
"""

# import of the needed functions
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import pandas as pd

def parse_measurements(file_path):
    """
    Loads a ascii-file and extracts the measured data into and data frame.
    The measurments are sorted along the time and the related I-mon at that time for each sweep/Series.

    Input: file path of the ascii file
    Output: structured data frame for future analysis and plotting
    """
    with open(file_path, "r") as file:
        content = file.readlines()

    # Initialisiere eine leere Liste, um DataFrames für jede Serie zu speichern
    series_dfs = []

    # Variablen zum Speichern des aktuellen Status
    series_name = None
    series_data = []

    # Iteriere durch die Zeilen und extrahiere die Daten
    for line in content:
        # Überprüfen, ob die Linie den Beginn einer neuen Serie markiert
        if line.startswith("Series_"):
            series_name = line.strip()
        elif line.startswith('"Index'):
            # Starte eine neue Sammlung von Daten
            series_data = []
        elif series_name and line.strip():  # Datenzeilen extrahieren
            # Teile die Zeile in Bestandteile auf
            parts = line.strip().split(',')
            try:
                # Überprüfen, ob die ersten beiden Einträge konvertierbar sind
                index = int(parts[0])
                time_s = float(parts[1])
                i_mon = float(parts[2])
                series_data.append([index, time_s, i_mon])
            except ValueError:
                # Ignoriere die Zeile, wenn eine Umwandlung fehlschlägt
                continue
        elif line.strip() == '' and series_name:
            # Wenn eine leere Zeile nach den Daten kommt, Serie abschließen
            if series_data:
                # Konvertiere die Daten der Serie in einen DataFrame
                df = pd.DataFrame(series_data, columns=["Index", "Time[s]", series_name])
                series_dfs.append(df)
            series_name = None

    # Zusammenführen der DataFrames basierend auf "Time[s]"
    if series_dfs:
        result_df = series_dfs[0][["Time[s]"]]  # Initialisiere mit der Zeitspalte
        for df in series_dfs:
            result_df = result_df.merge(df[["Time[s]", df.columns[-1]]], on="Time[s]")

        return result_df
    else:
        return pd.DataFrame()  # Leerer DataFrame, wenn keine Daten gefunden wurden

