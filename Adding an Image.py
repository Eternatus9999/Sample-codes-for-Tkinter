from tkinter import *
import customtkinter as ctk 
from PIL import Image #you need to run pip install Pillow in cmd to use this package
root = ctk.CTk()

root.title("Custom Icon")
root.geometry("600x600")

root.iconbitmap("Images/reindeer.ico")

my_Image = ctk.CTkImage(light_image=Image.open("Images/reindeer.png"), dark_image=Image.open("Images/reindeer.png"), size=(200, 200))

label = ctk.CTkLabel(root, text="", image=my_Image)
label.pack(pady=100)

root.mainloop()