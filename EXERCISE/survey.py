import tkinter as tk
from tkinter import SOLID, ttk,StringVar,messagebox

window = tk.Tk()
window.title("Survey")
window.geometry("500x600")

label_survey = ttk.Label(master=window,text="Survey",font="Calibri 28 ")
label_survey.grid(row=0,column=0,padx=20, pady=10)
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
result_label=ttk.Label(master=window, text="RESULT :", font='Calibri 12', foreground='green', relief ='raised')
result_label.grid(row=4, column=1, columnspan=2, padx=10, pady=10)

def on_select(event):
    selected = combo_box.get()
    global current_question
    current_question = selected
    if selected == "Maths":
        question_label.config(text = "Solve 2x + 8 = 10:")
    elif selected == "English":
        question_label.config(text = "Who is the author for Macbeth ? ")
    elif selected == "Science":
        question_label.config(text = "What is the chemical symbol for Oxygen ? ")


def submit_button_clicked():
    answer = answer_entry.get().strip()  
    if answer != "":
        if current_question == "Maths" and answer in ["x=1", "1"]:
            result_label.config(text = "Result : CORRECT!")
        elif current_question == "English" and answer.lower() in ["shakespeare", "william shakespeare"]:
            result_label.config(text = "Result : CORRECT!")
        elif current_question == "Science" and answer.upper() == "O2" and answer.lower() in ["o2"]:
            result_label.config(text = "Result : CORRECT!")
        else:
            result_label.config(text = "RESULT : Incorrect...Try again", foreground='red')
    else:
        messagebox.showwarning("No answer", "Please enter an answer.")


submit_button= ttk.Button(master=window, text="Submit", command=submit_button_clicked)
submit_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

combo_box.bind("<<ComboboxSelected>>", on_select)

current_question = None

window.mainloop()


