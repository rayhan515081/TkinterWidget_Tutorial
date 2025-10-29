import tkinter as tk
from tkinter import ttk,StringVar

# main window
window = tk.Frame()
window.title("Test")
window.geometry("700x700")

# defining function to show pages    
def show_page(page):
    for p in pages:
        p.pack_forget()
    page.pack(fill='both',expand=True)

# page 1
welcome_page=tk.Frame(window)
welcome_page.title("Welcome")
welcome_page.geometry("500x400")
welcome_label=tk.Label(master=welcome_page, text="Welcome to the IQ Test", font='Calibri 28 bold', borderwidth=1, relief='flat')
welcome_label.pack(padx=10,pady=10)
name_entry=tk.Entry(master=welcome_page,font='Calibri 16')
name_entry.pack(padx=10,pady=10)
cont_button=tk.Button(master=welcome_page,font='Calibri 16', text="Continue", command=lambda: show_page(window))
cont_button.pack(padx=10,pady=10)
back_button=tk.Button(master=welcome_page, text="Back", font='calibri 16',command=lambda: show_page(window))
back_button.pack(padx=10,pady=10)

# list for pages 
pages= [welcome_page,window]

# frame for radiobuttons
radiobutton_frame=tk.Frame(window)

# Title labels
label_heading=tk.Label(master=window, text="IQ Test", font='Calibri 28 bold', borderwidth=1, relief='flat')
label_heading.grid(row=0, column=0, padx=10,pady=10)

# question list
questions = [
    "1. If all Bloops are Razzies, and all Razzies are Lazzies, are all Bloops definitely Lazzies?",
    "2. What number comes next in the series: 2, 6, 12, 20, 30, ",
    "3. A cube has 6 faces. If you paint all faces and cut it into 27 smaller cubes, how many small cubes will have only one face painted?",
    "4. Rearrange the letters 'CIFAIPC' to form a word.",
    "5.Which one of the five is least like the other four?"]

entries =[]
# loop for labels and entries
for i, question in enumerate(questions):
        row=i*2+2
        label=tk.Label(master=window, text=question, font='Calibri 14', anchor='w', wraplength=500)
        label.grid(row=row,column=0, sticky='w',padx=10,pady=10)

        if question == questions[0]:
            var=StringVar()
            radio1 = tk.Radiobutton(radiobutton_frame,value =1,text='Yes', font = ("Calibri" ,14))
            radio2 = tk.Radiobutton(radiobutton_frame,value =2, text= 'No', font = ("Calibri" ,14))
            radio1.pack(anchor='w')
            radio2.pack(anchor='w')
            radiobutton_frame.grid(row=row+1,column=0,padx=10,pady=10)
        elif question == questions[4]:
            entry = ttk.Combobox(window, values =["Dog","Mouse","Lion","Snake","Elephant"], font='Calibri 14', state='readonly')
            entry.grid(row=row+1, column=0, padx=10, pady=10)
        else:
            entry = tk.Entry(window,font='Calibri 14')
            entry.grid(row=row+1, column=0, padx=10, pady=10)

entries.append(entry)

submit_button=tk.Button(master=window,text='Submit', width=10)
submit_button.grid(row=11, column=1, padx=10, pady=10)

window.mainloop()


