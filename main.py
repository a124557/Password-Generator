import random
import sqlite3
from tkinter import *

root = Tk()

# Creating a Label Widget and setting window title
myLabel = Label(root, text="Random Password Generator", font=("Arial", 20))
psswdNum = Label(root, text="Please enter desired number of passwords to generate")
root.title("Random Password Generator")
psswdLength = Label(root, text="Please enter desired password character length")
root.title("Random Password Generator")

# Window size
root.geometry('480x500')


# Handle button click event

chars = "abcdefghikjklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()0123456789"

def clicked():
    i = 0
    t.delete('1.0', END)
    while i < int(spin.get()):
        psswd = ""
        while len(psswd) < int(spin1.get()):
            psswd += chars[random.randint(0, len(chars) - 1)]
        t.insert(INSERT, "Password " + str(i + 1) + " : " + psswd + "\n")
        i += 1


# Adding button
btn = Button(root, text="Generate", command=clicked)

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# Description
myLabel.grid(column=0, row=1, pady=(0, 20))

psswdNum.grid(column=0, row=2,pady=(0, 10))
# Spinbox grid
# Spinbox for password length
spin = Spinbox(root, from_=0, to=20, width=5)
spin.grid(column=0, row=3, pady=(0, 10))
psswdLength.grid(column=0, row=4, pady=(0, 10))

# Spinbox for password character length
spin1 = Spinbox(root, from_=0, to=20, width=5)
# Spinbox grid
spin1.grid(column=0, row=5, pady=(0, 10))

# Button
btn.grid(column=0, row=6, pady=(0, 10))

# Create text widget for password output
t = Text(root, height=15, width=50)
t.grid(column=0, row=7, pady=20)


# Create scrollbar widget and set its command to text widget
scrollbar = Scrollbar(root, orient='vertical', command=t.yview())
scrollbar.grid(row=7, column=1, sticky='ns')

# Communicate back to scrollbar
t['yscrollcommand'] = scrollbar.set


# Prevent horizontal resizing
root.resizable(False, True)


# Create main Loop
root.mainloop()

