import matplotlib.pyplot as plt
from customtkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

students = [50, 40, 80, 60, 20]
labels = ["A", "B", "C", "D", "E"]

root = CTk()

root.geometry("800x400")
root.config(bg="#000000")

frame = CTkFrame(master=root)
frame.configure(bg_color="#000000")
frame.pack(pady=20, padx=20, fill="both", expand=True)

# Create the matplotlib Figure and Axes
fig, ax = plt.subplots()
ax.pie(students, labels=labels, autopct='%1.1f%%',textprops={'color': '#ffffff', 'fontsize': 12})
ax.set_title("Student Distribution")

fig.patch.set_facecolor("#000000")


# Embed the figure in the tkinter frame
canvas = FigureCanvasTkAgg(fig, master=frame)
canvas.draw()
canvas.get_tk_widget().pack(fill="both", expand=True)

root.mainloop()