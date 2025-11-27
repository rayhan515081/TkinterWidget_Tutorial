from encodings.punycode import T
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

window = tk.Tk()
window.title("Simple grading system")
window.geometry("800x700")

title_label = ttk.Label(master = window, text="Enter Student Grade:",font='Calibri 32 bold', borderwidth=1, relief='flat')
title_label.grid(row=0, column=1)
result_label=ttk.Label(master=window, text="GRADE:", font='Calibri 20 bold',foreground='green',borderwidth=5, relief='raised')
result_label.grid(row=7,column=1,pady=20, padx=20)

mark_label=ttk.Label(master=window, text='Mark(%) :', font='calibri 14', anchor='w')
mark_label.grid(row=4,column=0,padx=10,pady=10)
mark_entry=ttk.Entry(master=window,font='calibri 14')
mark_entry.grid(row=4,column= 1,padx=10,pady=10)

message=tk.Message(master=window, text="Enter a number between 0 and 100", width=200)

def get_button_1_text():
    mark_text=mark_entry.get()

    if mark_text.isdigit():
        mark=int(mark_text)

        if 0 <= mark <=100:
            if mark >= 90:
                result_label.config(text="GRADE: A")
            elif mark >= 80:
                result_label.config(text="GRADE: B")
            elif mark >= 70:
                result_label.config(text="GRADE: C")
            elif mark >= 60:
                result_label.config(text="GRADE: D")
            elif mark >= 50:
                result_label.config(text="GRADE: E")
            else:
                result_label.config(text="GRADE: F")
        else:
            messagebox.showwarning("Out of Range", "Enter a number between 0 and 100.")

    else:
        messagebox.showerror("Invalid Input", "Please enter numbers only.")
    
button_1=ttk.Button(master=window, text ='Submit',width=10,command = get_button_1_text)
button_1.grid(row = 5, column = 2,sticky ='se',padx=10,pady=10)

fields = ['First Name :', 'Last Name :','Subject :']

entries=[]


for i, field in enumerate(fields):
    label= ttk.Label(window, text=field, font='Calibri 14',anchor='w')
    label.grid(row=i+1, column=0, sticky='w',padx=10,pady=10)

    if field == "Subject :":
        entry = ttk.Combobox(window, values=["Math", "English", "Science","Computer Science"], font='Calibri 14', state='readonly')
    else:
        entry = ttk.Entry(window, font='Calibri 14')
    entry.grid(row=i+1, column=1, padx=10, pady=10)
    entries.append(entry)

def validate_name(name):
    if name.isalpha():
        return True
    return False

def on_submit():
    name = entries(0)(1).get()
    if not validate_name(name):
        messagebox.showerror("Invalid Input", 
                             "Name must contain only alphabets.")
    else:
        messagebox.showinfo("Valid Input",
                            "Name is valid.")

window.mainloop()