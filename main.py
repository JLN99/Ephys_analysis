'''
Starting Steps: 
    1. Enter/Create the virtuall enviroment: comand: pipenv shell
    -> opens or generates virt. envirment depending on the existing pipfile. - allways the same package versions
    2. lunching python files via the shell terminal: python filename.py 
    3. after editing or new code push to github!
'''
# import of needed packages and modules

import analysis as analysis             # file contains analysis functions
import matplotlib.pyplot as plt
import os
import numpy as np 

def read_values_from_file(file_path):
    with open(file_path, 'r') as file:
        values = [float(line.strip()) for line in file] 
    return values

def plot_values(values, title):
    values_new = [v * 10000 for v in values]
    plt.plot(values_new)
    plt.title(title)
    plt.xlabel('time [s]')
    plt.ylabel('Current [nA]')

    # Save the figure as an SVG file
    plt.savefig(title + ".svg", format="svg")

def main():
    folder_path = 'ascii-files'
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.asc'):  # Assuming ASCII files have .txt extension
            file_path = os.path.join(folder_path, file_name)
            values = read_values_from_file(file_path)
            plot_values(values, f'Plot of {file_name}')

if __name__ == '__main__':
    main()




# dfs_test = func.analyze_folder(folder_path)
# print(dfs_test)
# func.create_plot_area_under_trace(dfs_test)
# func.create_plot(dfs_test)