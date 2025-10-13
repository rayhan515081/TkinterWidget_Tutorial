import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Spinbox with Subjects")
window.geometry("400x400")

value_var = tk.DoubleVar()

display_label = ttk.Label(window, text="Selected Value: 0.00", font='Calibri 16 bold')
display_label.pack(pady=10)

def update_number_label(*args):
    value = value_var.get()
    display_label.config(text=f"Selected Value: {value:.2f}")

value_var.trace_add("write", update_number_label)

number_spinbox = ttk.Spinbox(window,from_=0,to=100,increment=0.01,textvariable=value_var,font='Calibri 18')
number_spinbox.pack(pady=10)

subjects = ("Math", "Science", "English", "History", "Art", "Computer Science")
subject_var = tk.StringVar(value=subjects[0])  

subject_label = ttk.Label(window, text=f"Selected Subject: {subjects[0]}", font='Calibri 16 bold')
subject_label.pack(pady=10)

def update_subject_label(*args):
    subject = subject_var.get()
    subject_label.config(text=f"Selected Subject: {subject}")

subject_var.trace_add("write", update_subject_label)

subject_spinbox = ttk.Spinbox(
    window,
    values=subjects,
    textvariable=subject_var,
    wrap=True,
    font='Calibri 18'
)
subject_spinbox.pack(pady=10)

window.mainloop()