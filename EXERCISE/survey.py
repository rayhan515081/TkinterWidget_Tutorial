import tkinter as tk
from tkinter import ttk,StringVar

# main window
window = tk.Tk()
window.title("Test")
window.geometry("700x700")

# defining function to show pages    
def show_page(page):
    pages = [welcome_page,quiz_page,result_page]
    for p in pages:
        p.pack_forget()
    page.pack(fill='both',expand=True)

# page 1
welcome_page=tk.Frame(window)
welcome_label=tk.Label(master=welcome_page, text="Welcome to the IQ Test", font='Calibri 28 bold', borderwidth=1, relief='flat')
welcome_label.pack(padx=10,pady=10)
name_label=tk.Label(welcome_page,text="Enter your name:", font='Calibri 16')
name_label.pack(padx=10,pady=10)
name_entry=tk.Entry(master=welcome_page,font='Calibri 16')
name_entry.pack(padx=10,pady=10)
cont_button=tk.Button(master=welcome_page,font='Calibri 16', text="Continue", command=lambda: show_page(welcome_page))
cont_button.pack(padx=10,pady=10)

# frame for radiobuttons
radiobutton_frame=tk.Frame(window)

# page 2
quiz_page=tk.Frame(window)
label_heading=tk.Label(master=quiz_page, text="IQ Test", font='Calibri 28 bold', borderwidth=1, relief='flat')
label_heading.grid(row=0, column=0, padx=10,pady=10)

# question list
questions = [
    "1. If all Bloops are Razzies, and all Razzies are Lazzies, are all Bloops definitely Lazzies?",
    "2. What number comes next in the series: 2, 6, 12, 20, 30, ",
    "3. A cube has 6 faces. If you paint all faces and cut it into 27 smaller cubes, how many small cubes will have only one face painted?",
    "4. Rearrange the letters 'CIFAIPC' to form a word.",
    "5.Which one of the five is least like the other four?"]
# correct answers
answers = [
    "Yes",
    "42",
    "6",
    "PACIFIC",
    "Snake"
]

user_inputs=[]

entries =[]
# loop for labels and entries
for i, question in enumerate(questions):
        row=i*2+2
        label=tk.Label(master=quiz_page, text=question, font='Calibri 14', anchor='w', wraplength=500)
        label.grid(row=row,column=0, sticky='w',padx=10,pady=10)

        if question == questions[0]:
            var=StringVar()
            radio1 = tk.Radiobutton(radiobutton_frame,value ='Yes',text='Yes',variable=var, font = ("Calibri" ,14))
            radio2 = tk.Radiobutton(radiobutton_frame,value ='No',variable=var,text= 'No', font = ("Calibri" ,14))
            radio1.pack(anchor='w')
            radio2.pack(anchor='w')
            radiobutton_frame.grid(row=row+1,column=0,padx=10,pady=10)
        elif question == questions[4]:
            entry = ttk.Combobox(quiz_page, values =["Dog","Mouse","Lion","Snake","Elephant"], font='Calibri 14', state='readonly')
            entry.grid(row=row+1, column=0, padx=10, pady=10)
        else:
            entry = tk.Entry(quiz_page,font='Calibri 14')
            entry.grid(row=row+1, column=0, padx=10, pady=10)

entries.append(entry)
user_inputs.append(entry)

submit_button=tk.Button(master=quiz_page,text='Submit', width=10,command =lambda:show_page())
submit_button.grid(row=11, column=1, padx=10, pady=10)

# page 3
result_page=tk.Frame(window)

window.mainloop()


