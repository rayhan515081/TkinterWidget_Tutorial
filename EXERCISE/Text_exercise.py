import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.tile('Tkinter Tk_text Widget')
window.geometry('400x400')

myCombobox =tk.Text(master=window, undo=True, maxundo=100, spacing1=10,spacing2=2, spacing3=5,height=5, wrap='char')

myCombobox.pack()




