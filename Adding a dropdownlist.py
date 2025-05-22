from tkinter import *
from tkinter.ttk import *

root = Tk()

root.title("Form for student registering")

root.geometry("400x400")

lbl = Label(root, text="Name: ")

choices = ["Java", "Python", "C++", "C#", "PHP", "Ruby", "JavaScript", "HTML", "CSS"] 

subject_dropdown = Combobox(root, values= choices)

txt = Entry(root, width=10)

lbl.grid()
txt.grid(column=1, row=0, padx=10, pady=10,)
subject_dropdown.grid(column=1, row=2)

# To get values from the dropdownlist you have to use the get() method

root.mainloop()
