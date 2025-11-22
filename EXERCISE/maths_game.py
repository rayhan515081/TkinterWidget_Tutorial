# Import Tkinter Libraries
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import random
import os

# Create Window with title and set size of window
Mode = "None"
window = tk.Tk()
window.title('Simple Math Game')
window.geometry('700x400')
window.resizable(False, False)
window.configure(bg='#925FB0')

# ===== Helper Function to Load and Resize Images =====
def load_image(path, size=(75, 75)):
    """Safely load and resize an image, returning a PhotoImage."""
    if not os.path.exists(path):
        print(f"Image not found: {path}")
        return None
    img = Image.open(path)
    img = img.resize(size)
    return ImageTk.PhotoImage(img)

# ===== Function to Generate Random Question =====
def RandQ():
    # Generate Random First Number
    image_paths = [f"maths_game/{i}.png" for i in range(10)]

    # First Number Image
    num1_path = random.choice(image_paths)
    num1 = load_image(num1_path)
    if num1:
        label1 = tk.Label(window, image=num1)
        label1.image = num1
        label1.place(x=225, y=125, width=75, height=75)

    # Second Number Image
    num2_path = random.choice(image_paths)
    num2 = load_image(num2_path)
    if num2:
        label2 = tk.Label(window, image=num2)
        label2.image = num2
        label2.place(x=400, y=125, width=75, height=75)

    # Equals Sign Image
    equals_path = r"maths_game/equals.png"
    equals = load_image(equals_path)
    if equals:
        equalLabel = tk.Label(window, image=equals)
        equalLabel.image = equals
        equalLabel.place(x=495, y=125, width=75, height=75)

# ===== Function to Start the Game Depending on Mode =====
def Start():
    global Mode
    if Mode == "Mul":
        RandQ()
        print("Mul")
        oper_path = r"maths_game/multiply.png"
    elif Mode == "Div":
        RandQ()
        print("Div")
        oper_path = r"maths_game/divide.png"
    elif Mode == "Add":
        RandQ()
        print("Add")
        oper_path = r"maths_game/plus.png"
    elif Mode == "Sub":
        RandQ()
        print("Sub")
        oper_path = r"maths_game/minus.png"
    elif Mode == "None":
        print("None")
        return
    else:
        print("Error")
        return

    # Display Operator Image
    oper = load_image(oper_path)
    if oper:
        operLabel = tk.Label(window, image=oper)
        operLabel.image = oper
        operLabel.place(x=315, y=125, width=75, height=75)

# ===== Functions for Each Mode =====
def Mul():
    global Mode
    Mode = 'Mul'
    Start()

def Div():
    global Mode
    Mode = 'Div'
    Start()

def Add():
    global Mode
    Mode = 'Add'
    Start()

def Sub():
    global Mode
    Mode = 'Sub'
    Start()

# ===== Buttons for Selecting Mode =====
mul_img = tk.PhotoImage(file="maths_game/multiply.png")
div_img = tk.PhotoImage(file="maths_game/divide.png")
add_img = tk.PhotoImage(file="maths_game/plus.png")
sub_img = tk.PhotoImage(file="maths_game/minus.png")

btnm = tk.Button(window, image=mul_img, command=Mul)
btnm.image = mul_img
btnm.place(x=30, y=20, width=125, height=60)

btnd = tk.Button(window, image=div_img, command=Div)
btnd.image = div_img
btnd.place(x=30, y=100, width=125, height=60)

btna = tk.Button(window, image=add_img, command=Add)
btna.image = add_img
btna.place(x=30, y=180, width=125, height=60)

btns = tk.Button(window, image=sub_img, command=Sub)
btns.image = sub_img
btns.place(x=30, y=260, width=125, height=60)


# ===== Entry Widget and Submit Button =====
answer = tk.Entry(window, font=("Arial", 20))
answer.place(x=300, y=220, width=100, height=50)

def store_input():
    user_input = answer.get()
    print(f"User entered: {user_input}")
    answer.delete(0, tk.END)

btnsubmit = tk.Button(window, text="Submit", command=store_input)
btnsubmit.place(x=450, y=300, width=100, height=50)

# ===== Run the Window Loop =====
window.mainloop()




