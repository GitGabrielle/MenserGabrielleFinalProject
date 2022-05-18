# Basic Habit Tracker - By Gabrielle Menser
# Initiate Tkinter
# pip install pillow

from tkinter import *
from PIL import ImageTk, Image

# Main Window(1)

window = Tk()
window.geometry("400x300")
window.title("Habit Tracker")

# Image1

img = Image.open("C:/Users/gmenser1/Pictures/IMG1.png")
photo = ImageTk.PhotoImage(img)
lab = Label(image=photo)
lab.pack()

# Window1 Label(1)

label1 = Label(window, text="Habits", font=("arial", 16, "bold"))

# Window1 Label(2)

label2 = Label(window, text="It takes 66 days for a habit to become automatic!", font=("arial", 12))
label2.place(x=30, y=60)

# Window1 Label(3)

label3 = Label(window, text="WELCOME!", font=("arial", 16, "bold"))
label3.place(x=130, y=20)

# Exit Function for button1


def exit1():
    exit()

# Function for Window(2)


def second_win():
    window = Tk()
    window.geometry("400x300")
    window.title("Let's build habits!")

# Window(2) Label

    label4 = Label(window, text="What have you accomplished today?", font=("arial", 16, "bold"))
    label4.place(x=10, y=20)

# Window(2) Checkboxes

    c1 = Checkbutton(window, text="Meditate").place(x=80,y=60)
    c2 = Checkbutton(window, text="Stretch").place(x=80, y=80)
    c3 = Checkbutton(window, text="Exercise").place(x=80, y=100)
    c4 = Checkbutton(window, text="Read").place(x=80, y=120)
    c5 = Checkbutton(window, text="Drink 1 Gallon of Water").place(x=80, y=140)
    c6 = Checkbutton(window, text="8 Hours of Sleep").place(x=80, y=160)

# Window(2) Buttons

    button3 = Button(window, text="Nevermind", fg='white', bg="black", relief=RAISED, command=exit1, font=("arial", 12, "bold"))
    button3.place(x=200, y=210)
    button4 = Button(window, text="I DID IT!", fg='white', bg="black", relief=RAISED, command=third_win, font=("arial", 12, "bold"))
    button4.place(x=100, y=210)

# Button(1)

button1 = Button(window, text="Nevermind", fg='white', bg="black", relief=RAISED, command=exit1, font=("arial", 12, "bold"))
button1.place(x=200, y=110)

# Button(2)

button2 = Button(window, text="TRACK", fg='white', bg="black", relief=RAISED, command=second_win, font=("arial", 12, "bold"))
button2.place(x=100, y=110)


# Function for Window(3)

def third_win():
    window = Tk()
    window.geometry("200x200")
    window.title("CONGRATULATIONS!")

# Window(3) Label

    label5=Label (window, text="YOU DID IT!", font=("arial", 16, "bold"))
    label5.place(x=10, y=20)

# Window(3) Buttons

    button3 = Button(window, text="Goodbye!", fg='white', bg="black", relief=RAISED, command=exit1, font=("arial", 12, "bold"))
    button3.place(x=100, y=100)


window.mainloop()

