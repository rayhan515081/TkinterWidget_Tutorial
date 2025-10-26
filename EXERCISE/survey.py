import tkinter as tk
from tkinter import ttk,StringVar,messagebox

window = tk.Tk()
window.title("Survey")
window.geometry("500x600")

label_survey = ttk.Label(master=window,text="Survey",font="Calibri 28 bold")
label_survey.grid(row=0,column=0,padx=10, pady=10)
label_prompt = ttk.Label(master=window,text="What's your favourite subject?",font="Calibri 14")
label_prompt.grid(row=1,column=0,padx=10, pady=10)

string_var=tk.StringVar()

combo_box = ttk.Combobox(master=window,textvariable=string_var, values =["Maths","English","Science"],font="Calibri 12",state='readonly')
combo_box.grid(row=1, column=1,padx=10,pady=10)
 
# Questions
question_label= ttk.Label(master=window, text="", font='Calibri 12')
question_label.grid(row=2, column=0,padx=10, pady =10)
answer_entry = ttk.Entry(master=window, font='Calibri 12')
answer_entry.grid(row=2, column=1,padx=10, pady =10)

submit_button= ttk.Button(master=window, text="Submit", command=submit_button_clicked)
submit_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

def on_select(event):
    selected = combo_box.get()
    global current_question
    current_question = selected
    if selected == "Maths":
        question_label.config(text = "Solve 2x + 8 = 10:")
    elif selected == "English":
        question_label.config(text = "Who is the author for Macbeth ?:")
    elif selected == "Science":
        question_label.config(text = "What is the chemical symbol for Oxygen ?:")



def submit_button_clicked():
    answer = answer_entry.get()
    if answer == "":
        if current_question == "Maths" and answer == "x=1" or "1":
            print("Correct!")
            return
        elif current_question == "English" and answer == "Shakespeare" or "William Shakespeare" or "shakespeare" or "william shakespeare":
            print("Correct!")
            return
        elif current_question == "Science" and answer == "O2":
            print("Correct!")
            return
    else :
        messagebox.showerror("Incorrect,Try again...")

combo_box.bind("<<ComboboxSelected>>", on_select)

current_question = None

window.mainloop()


