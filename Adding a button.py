from tkinter import *

root = Tk()

root.title("Welcome to Chathusha")

root.geometry("1920x1800")

lbl = Label(root, text="Chathusha")
lbl.grid()

def clicked():
    lbl.configure(text="Button Clicked")

btn = Button(root, text="Click Me", fg = "red", command=clicked)
btn.grid(column=1, row=0)

root.mainloop()