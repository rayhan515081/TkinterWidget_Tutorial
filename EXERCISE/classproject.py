import tkinter as tk
from tkinter import BooleanVar, DoubleVar, IntVar, StringVar, ttk

window = tk.Tk()
window.title("Stock System")
window.geometry("500x500")

String_var= tk.StringVar()
double_var= tk.DoubleVar()
int_var= tk.IntVar()
bool_var= tk.BooleanVar()


fields = ['Product ID' ,'Product Name', 'Product Description' ,'Price' ,'Quantity' ,'Limited']

entries=[]

for i, field in enumerate(fields):
    label = ttk.Label(window, text = field , font = 'calibri 24 bold', anchor = 'w')
    label.grid(row=i+1, column=0, sticky='w', padx=10, pady=10)

# text entry boxes
text_entry1= ttk.Entry(window,textvariable = StringVar(), font='calibri 14')
text_entry1.grid(row = 1, column=0, padx=10, pady=10)

text_entry2= ttk.Entry(window,textvariable = StringVar(), font='calibri 14')
text_entry2.grid(row = 1, column=1, padx=10, pady=10)

text_entry3= ttk.Entry(window,textvariable = StringVar(), font='calibri 14')
text_entry3.grid(row = 1, column=1, padx=10, pady=10)

text_entry4= ttk.Entry(window,textvariable = DoubleVar(), font='calibri 14')
text_entry4.grid(row = 1, column=3, padx=10, pady=10)

text_entry5= ttk.Entry(window,textvariable = IntVar, font='calibri 14')
text_entry5.grid(row = 1, column=4, padx=10, pady=10)

text_entry6= ttk.Entry(window,textvariable = BooleanVar, font='calibri 14')
text_entry6.grid(row = 1, column=5, padx=10, pady=10)



 




