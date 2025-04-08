
from tkinter import *

root = Tk()
root.title("Text Editor")

text = Text(root)
text.pack()

def save():
    with open("text.txt","w") as f:
        f.write(text.get(1.0, END))

Button(root, text="Save", command=save).pack()
root.mainloop()