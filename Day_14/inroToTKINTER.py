# import tkinter
from tkinter import *

# window = tkinter.Tk() ---- if you only do -> (import turtle)
window = Tk()
window.minsize(width=500, height= 300)

# LABEL
label = Label(text="I am a label." , font= ("Arial",24,"bold"))
# label.pack(side = "bottom")
# label.pack(expand=True)
label.pack() # For printing

# BUTTON
def button_clicked():
    print("Button clicked!")
    new_text = input.get()
    # label.config(text= "Button got clicked!")
    label.config(text= new_text)
button = Button(text="Click me" , command=button_clicked)
button.pack()  

# ENTRY
input = Entry(width=10)
input.pack()

window.mainloop()