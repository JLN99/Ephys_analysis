# GUI

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