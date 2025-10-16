import tkinter as tk
from tkinter import BooleanVar, DoubleVar, IntVar, StringVar, ttk

class products:
  def __init__(self,Product_ID, name, description, price, quantity, limited):
       self.Product_id = id
       self.name = name
       self.description = description
       self.price = float(price)
       self.quantity = int(quantity)
       self.limited = bool(limited)

       def __str__(self):
           return f"{self.product_id} - {self.name} (${self.price:.2f)}")
window = tk.Tk()
window.title("Stock System")
window.geometry("600x700")

String_var= tk.StringVar()
double_var= tk.DoubleVar()
int_var= tk.IntVar()
bool_var= tk.BooleanVar()

# labels
fields = ['Product ID' ,'Product Name', 'Product Description' ,'Price' ,'Quantity' ,'Limited']

entries=[]

for i, field in enumerate(fields):
    label = ttk.Label(window, text = field , font = 'calibri 16 bold', anchor = 'w')
    label.grid(row=i+1, column=0, sticky='w', padx=10, pady=10)

# spinboxes
price_spinbox=ttk.Spinbox(window, from_=0, to=1000, increment=1, textvariable = double_var, font='calibri 14')
price_spinbox.grid (row=4, column=1, padx=10, pady=10)
quantity_spinbox=ttk.Spinbox(window, from_=0, to_= 100000,increment=1,textvariable= int_var, font='calibri 14')
quantity_spinbox.grid(row=5, column=1, padx=10, pady=10)

combo_box=ttk.Combobox(window,textvariable = bool_var,values=["True","False"],state='readonly' ,font='calibri 14')
combo_box.grid(row=6,column=1, padx=10,pady=10)

# text entry boxes
text_entry1= ttk.Entry(window,textvariable = StringVar(), font='calibri 14')
text_entry1.grid(row = 1, column=1, padx=10, pady=10)

text_entry2= ttk.Entry(window,textvariable = StringVar(), font='calibri 14')
text_entry2.grid(row = 2, column=1, padx=10, pady=10)

text_entry3= ttk.Entry(window,textvariable = StringVar(), font='calibri 14')
text_entry3.grid(row = 3, column=1, padx=10, pady=10)

window.mainloop()


 




