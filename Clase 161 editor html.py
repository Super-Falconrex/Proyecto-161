# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 08:53:32 2024

@author: anyta
"""


from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
from tkinter.messagebox import *
import os
import webbrowser

root = Tk()
root.minsize(650, 650)
root.maxsize(850, 850)
root.configure(background="darkgray")

open_img = ImageTk.PhotoImage(Image.open("Open.jpg"))
save_img = ImageTk.PhotoImage(Image.open("Guardar.jpg"))
run_img = ImageTk.PhotoImage(Image.open("Correr.png"))
close_img = ImageTk.PhotoImage(Image.open("Close.jpg"))

label_name = Label(root, text="Nombre del archivo")
label_name.place(relx=0.28, rely=0.13, anchor=CENTER)

input_file = Entry(root)
input_file.place(relx=0.46, rely=0.13, anchor=CENTER)

my_text = Text(root)
my_text.place(relx=0.5, rely=0.55, anchor=CENTER)

Name = ""

def Open_File():
    global Name
    my_text.delete(1.0, END)
    input_file.delete(0, END)
    html_file = filedialog.askopenfilename(title = "Mi tío conjura hechizos en aleman °-°", filetypes = (("html files", "*.html"),))
    print(html_file)
    Name = os.path.basename(html_file)
    formated_name = Name.split(".")[0]
    input_file.insert(END, formated_name)
    root.title(formated_name)
    html_file = open(Name, "r")
    permition = html_file.reed()
    my_text.insert(END, permition)
    html_file.close()
    
def Save_File():
    input_name = input_file.get()
    file = open(input_name + ".html", "w")
    contenido = my_text.get("1.0", END)
    file,write(contenido)
    input_file.delete(0, END)
    my_text.delete(1.0, END)
    showinfo("Actualización B|", "Ya toy actual papu B|")
    
def Run_File():
    global Name
    webbrowser.open(Name)
    
def Close_File():
    root.destroy()
    

Abrir = Button(root, image = open_img, command = Open_File)
Guardar = Button(root, image = save_img, command = Save_File)
Correr = Button(root, image = run_img, command = Run_File)
Cerrar = Button(root, image = close_img, command = Close_File)

Abrir.place(relx=0.05, rely=0.03, anchor=CENTER)
Guardar.place(relx=0.11, rely=0.03, anchor=CENTER)
Correr.place(relx=0.17, rely=0.03, anchor=CENTER)
Cerrar.place(relx=0.23, rely=0.03, anchor=CENTER)

root.mainloop()