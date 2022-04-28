
# Import module
from tkinter import *
  
# Create object
root = Tk()
  
# Adjust size
root.geometry( "200x200" )
  
# Change the label text
def show():
    text = clicked.get()
    ent.insert(0,text)
    label.config( text = clicked.get() )
  
# Dropdown menu options
options = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]
  
# datatype of menu text
clicked = StringVar()
  
# initial menu text
# clicked.set( "Monday" )
  
# Create Dropdown menu
drop = OptionMenu( root , clicked , *options,command=show)
drop.pack()
ent = Entry(root)
ent.pack()
# text = clicked.get()
# ent.insert(0,text)
# Create button, it will change label text
# button = Button( root , text = "click Me" , command = show ).pack()
  
# Create Label
label = Label( root , text = " " )
label.pack()
  
# Execute tkinter
root.mainloop()