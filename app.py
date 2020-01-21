import tkinter as tk 
from tkinter import filedialog, Text
import os

root = tk.Tk()

canvas = tk.Canvas(root, height = 700, width = 700, bg = "SkyBlue1")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx = 0.1, rely = 0.1)

open_file = tk.Button(root, text = "Open File", padx = 10, pady = 5,
                         fg = "white",bg = "#263D42")
open_file.pack()
root.mainloop()