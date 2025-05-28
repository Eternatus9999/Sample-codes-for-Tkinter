from customtkinter import *
from tkinter import ttk

window = CTk()

window.geometry('800x400')

table = ttk.Treeview(window, columns=["ID", "Name", "Category", "Price"], show="headings")

table.heading("ID", text="ID")
table.heading("Name", text="Name")
table.heading("Category", text="Category")
table.heading("Price", text="Price")

products = [
    ("P001", "SunnyThoughts", "Male", "Rs.100"),
    ("P002", "MoonWhispers", "Female", "Rs.120"),
    ("P003", "OceanBreeze", "Unisex", "Rs.150"),
    ("P004", "ForestGlow", "Male", "Rs.110"),
    ("P005", "VelvetDawn", "Female", "Rs.130"),
    ("P006", "CitrusSpark", "Unisex", "Rs.140"),
    ("P007", "CrimsonVibe", "Male", "Rs.115"),
    ("P008", "LilyEcho", "Female", "Rs.125"),
    ("P009", "TwilightMist", "Unisex", "Rs.135"),
    ("P010", "AmberSoul", "Male", "Rs.105"),
    ('P011', 'CitrusSpark', 'Male', 'Rs.124'),
    ('P012', 'ForestGlow', 'Female', 'Rs.148'),
    ('P013', 'ForestGlow', 'Male', 'Rs.182'),
    ('P014', 'EarthTone', 'Female', 'Rs.186'),
    ('P015', 'SilverRush', 'Female', 'Rs.198'),
    ('P016', 'ForestGlow', 'Female', 'Rs.145'),
    ('P017', 'TwilightMist', 'Male', 'Rs.169'),
    ('P018', 'ShadowLight', 'Male', 'Rs.116'),
    ('P019', 'ForestGlow', 'Female', 'Rs.125'),
    ('P020', 'EarthTone', 'Male', 'Rs.132'),
]


for product in products:
    table.insert("", "end", values=product)
table.pack()


def printlist():
    selected = table.selection()
    for item in selected:
            values = table.item(item)["values"]
            print(values)

button = CTkButton(master=window, text="Print", command=printlist)
button.pack()

window.mainloop()