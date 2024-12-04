'''
Starting Steps: 
    1. Enter/Create the virtuall enviroment: comand: pipenv shell
    -> opens or generates virt. envirment depending on the existing pipfile. - allways the same package versions
    2. lunching python files via the shell terminal: python filename.py 
    3. after editing or new code push to github!
'''
# import of needed packages and modules

import functions as func                # file contains the functions created
import matplotlib.pyplot as plt

folder_path = 'C:\\Users\\julia\\lokales-Archiv\\PhD\\Phython-test\\files\\20240620_a1b2g2-EtOH-1h_zelle2.asc'


df = func.asc_to_df(folder_path)

func.max_current_per_series(df)

# df.info()
# print(df.head())




# dfs_test = func.analyze_folder(folder_path)
# print(dfs_test)
# func.create_plot_area_under_trace(dfs_test)
# func.create_plot(dfs_test)