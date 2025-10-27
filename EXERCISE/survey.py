import tkinter as tk
from tkinter import ttk,StringVar

window = tk.Tk()
window.title("Test")
window.geometry("800x700")

radiobutton_frame=tk.Frame(window)

# Title labels
label_heading=ttk.Label(master=window, text="IQ Test", font='Calibri 28 bold', borderwidth=1, relief='flat')
label_heading.grid(row=0, column=1, padx=10,pady=10)
label_sub=ttk.Label(master=window , text='Find Your IQ', font = 'Calibri 24', borderwidth=1, relief='flat')
label_sub.grid(row=1, column=1, padx=10, pady=10)

# question labels
questions = [
    "1. If all Bloops are Razzies, and all Razzies are Lazzies, are all Bloops definitely Lazzies?",
    "2. What number comes next in the series: 2, 6, 12, 20, 30, ",
    "3. A cube has 6 faces. If you paint all faces and cut it into 27 smaller cubes, how many small cubes will have only one face painted?",
    "4. Rearrange the letters 'CIFAIPC' to form a word.",
    "5.Which one of the five is least like the other four?"]

entries =[]

for i, question in enumerate(questions):
        label=ttk.Label(master=window, text=question, font='Calibri 16', anchor='w', wraplength=500)
        label.grid(row=i+1,column=0, sticky='w',padx=10,pady=10)

        if question == questions[0]:
            var=StringVar()
            radio1 = ttk.Radiobutton(radiobutton_frame,value =1,text='No')
            radio2 = ttk.Radiobutton(radiobutton_frame,value =2, text= 'Yes')
            radio1.pack(anchor='w')
            radio2.pack(anchor='w')
            radiobutton_frame.grid(row=i+1,column=1,padx=10,pady=10)
        elif question == questions[4]:
            entry = ttk.Combobox(window, values =["Dog","Mouse","Lion","Snake","Elephant"], font='Calibri 14', state='readonly')
        else:
            entry = ttk.Entry(window,font='Calibri 14')
        entry.grid(row=i+1, column=1, padx=10, pady=10)

entries.append(entry)

window.mainloop()


