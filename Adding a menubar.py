from tkinter import *

root = Tk()

root.title("Chathusha Pehemina")

root.geometry("400x400")

menu = Menu(root)

item = Menu(menu, tearoff = 0 ) #tearoff is used to remove the line which is clickable and the command will make a popup window with options
menu.add_cascade(label="File", menu=item, underline=0)
item.add_command(label="New",command=None)
item.add_command(label="Open",command=None)
item.add_command(label="Save",command=None)
item.add_separator() #used to add a line
item.add_command(label="Exit",command=root.destroy)

root.config(menu=menu)

root.mainloop()