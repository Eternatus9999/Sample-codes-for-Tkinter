from tkinter import *

root = Tk()

root.title("Welcome to Chathusha")

root.geometry("1920x1800")

lbl = Label(root, text="Chathusha")
lbl.grid()

def clicked():
    lbl.configure(text="Button Clicked")

btn = Button(root, text="Click Me", fg = "red", bg= "yellow", command=clicked, activebackground="lime", activeforeground="blue")
btn.config(state=ACTIVE) # to enable the button(ACTIVE/DISABLED)

# To add Image to a button

# image = PhotoImage(file="button.png")
# btn.config(image=image)
# btn.config(compound=LEFT)

btn.grid(column=1, row=0)

root.mainloop()