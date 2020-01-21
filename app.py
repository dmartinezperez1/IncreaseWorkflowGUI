
import tkinter as tk 
from tkinter import filedialog, Text
import os

#create the root window
root = tk.Tk()
#create a list to store the apps you want to start
apps = []

#Function to open file explorer and selecte apps you want to add
def addApp():
    #delete previous list contents to avoid duplication
    for widget in frame.winfo_children():
        widget.destroy()
    #Add functionality to "Open Apps" button and limit the user to only selcting executables
    filename= filedialog.askopenfilename(initialdir = "/", title = "Select File",
                                         filetypes = (("executables","*.exe"), ("all files", "*.*")))
    
    #Add selected apps in the list created above 
    apps.append(filename)
    print(filename)
    #Loop so the user can add as many apps as they want. 
    for app in apps:
        label = tk.Label(frame, text = app, bg = "gray")
        label.pack()
#Function to be able to start/run apps
def run_apps():
    for app in apps:
        os.startfile(app)

#The main background of the GUI
canvas = tk.Canvas(root, height = 700, width = 700, bg = "SkyBlue1")
canvas.pack()

#Create a box that is centered in the GUI where the text will go.
frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx = 0.1, rely = 0.1)

#Create the button to open File Explorer to find executables to add.
open_file = tk.Button(root, text = "Open File", padx = 10, pady = 5,
                         fg = "white",bg = "#263D42", command = addApp)
open_file.pack()

#Create the button that will start the programs selected. 
run_apps = tk.Button(root, text = "Run Apps", padx = 10, pady = 5,
                        fg = "white", bg = "#263D42", command = run_apps)
run_apps.pack()

root.mainloop()
