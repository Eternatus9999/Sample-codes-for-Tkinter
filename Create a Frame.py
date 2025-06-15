from tkinter import *

root = Tk()

root.title("Printer")

root.geometry("400x400")

frame = Frame(root, bg="black")
frame.place(relx=0.5, rely=0.5, anchor=CENTER)

button_frame = Frame(frame, bg="red")
button_frame.pack(side=TOP)

root.mainloop()