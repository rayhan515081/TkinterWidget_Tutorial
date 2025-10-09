import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('Tkinter Tk_text Widget')
window.geometry('400x400')

myCombobox =tk.Text(master=window, undo=True, maxundo=1, spacing1=100,spacing2=10, spacing3=5,height=1, wrap='none')

myCombobox.pack()

window.mainloop()