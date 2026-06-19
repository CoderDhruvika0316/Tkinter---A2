from tkinter import *
from datetime import date 

window = Tk()
window.title("Getting Started With Widgets")
window.geometry("500x500")

ME = Label(text = "Hello!", fg = "black", bg = "light pink", width = 300, height = 1)
my_name = Label(text = "Enter your name:", bg = "pink")
my_entry = Entry()

def display():
    name = my_entry.get()
    global message 
    message = "\nWelcome to the Tkinter Application!\nToday's date is:"
    my_greeting = f"Hello {name}!"

    my_text.insert(END, my_greeting)
    my_text.insert(END, message)
    my_text.insert(END, date.today())

my_text = Text(height = 3)
my_button = Button(text = "Submit", command = display, height = 1, fg = "black", bg = "light pink")

ME.pack()
my_name.pack()
my_entry.pack()
my_button.pack()
my_text.pack()

window.mainloop()