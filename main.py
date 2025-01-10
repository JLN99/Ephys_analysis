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

folder_path = 'ascii-files'


df = analysis.analyze_folder(folder_path)

print(df.items())

# analysis.max_current_per_series(df)

# df.info()
# print(df.head())




# dfs_test = func.analyze_folder(folder_path)
# print(dfs_test)
# func.create_plot_area_under_trace(dfs_test)
# func.create_plot(dfs_test)