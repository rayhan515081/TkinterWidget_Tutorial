import tkinter as tk
from tkinter import ttk,StringVar

window = tk.Tk()
window.title("Survey")
window.geometry("500x600")

label_survey = ttk.Label(master=window,text="Survey",font="Calibri 20 bold")
label_survey.grid(row=0,column=0,padx=10, pady=10)
label_prompt = ttk.Label(master=window,text="Select an option from the Combobox.",font="Calibri 12")
label_prompt.grid(row=1,column=0,padx=10, pady=10)

string_var=tk.StringVar()

combo_box = ttk.Combobox(master=window,textvariable=string_var, values =["Maths","English","Science"],font="Calibri 12",state='readonly')
combo_box.grid(row=2, column=0,padx=10,pady=10)

def get_combo_selected(event):
    selected_value=combo.get()
    if
   
    

window.mainloop()


