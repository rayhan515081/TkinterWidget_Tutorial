import tkinter as tk
from tkinter import ttk

window=tk.Tk()
window.title("Tkinter Combobox Widget")
window.geometry('400x400')

string_var = tk.StringVar()
myCombobox =ttk.Combobox(master=window, textvariable = string_var,values=["This option","That Option","Another Option"])

def get_update_label():
    selected = myCombobox.get()
    label.config(text=f"You selected: {selected}")

window.mainloop()



