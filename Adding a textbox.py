from tkinter import *

root = Tk()

root.title("Welcome to Chathusha Pehemina")

root.geometry("1920x1800")

lb1 = Label(root, text="Chathusha Pehemina")

lb1.grid()

txt = Entry(root, width=10)
txt.grid(column=1, row=0)

def clicked():
    res = "You worte" + txt.get()
    lb1.configure(text=res)

btn = Button(root, text = "Click me", fg = "red", command = clicked)
btn.grid(column=0, row=1)

root.mainloop()