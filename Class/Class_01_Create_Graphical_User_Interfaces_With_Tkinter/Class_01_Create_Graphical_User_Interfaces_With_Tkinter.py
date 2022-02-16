from tkinter import *
# from tkinger import everything

"""
    -> In Kinter everthing is a widget , button widget, text widget
"""

root =Tk()
# this have to go first, this has to happen before anything any thing in you porgram

# to display the widget there is a two step 
# first you have to define 
# second put it onto the screen

# first:
myLabel=Label(root,text="Hello World!")
# here we created the Label widget in the root widget

#second:
# there is a couple of why to put thing in the secreen using tkinter
# first let's talk about the pack
myLabel.pack()
root.mainloop()
# and then run that into a loop
