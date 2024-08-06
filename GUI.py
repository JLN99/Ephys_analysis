# GUI
'''
Code for the implementation of a GUI.
The GUI should make the importation of the folder path, the analysis and the plot genaration easy accessible.
Still to implement:
    1. selection of folder path which should be analyzed
    2. Checkbox system to decide in which way the data should be analyzed and displayed
    3. selection/creation of the result folder where the analysis summary and plots should be stored
'''
import customtkinter as ctki
from customtkinter import filedialog

ctki.set_appearance_mode("dark") # background/generall color mode
ctki.set_default_color_theme("green") # color mode of buttons/field etc.

root = ctki.CTk()
root.geometry("500x350") # size of the GUI

def load_ascii():
    print("test")

frame = ctki.CTkFrame(master = root)
frame.pack(pady =20, padx=60, fill="both", expand=True)

label = ctki.CTkLabel(master=frame, text="Load ASCII-files")
label.pack(pady=12, padx=10)

entry1 = ctki.CTkEntry(master=frame, placeholder_text="Select folder")
entry1.pack(pady=12,padx=10)
filedialog.askdirectory()


button = ctki.CTkButton(master=frame, text="load files")
button.pack(pady=12, padx=10)

root.mainloop()