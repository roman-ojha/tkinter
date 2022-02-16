from tkinter import *
root=Tk()

def myClick():
    myLabel=Label(root,text="Clicked!!",fg="red")
    myLabel.pack()

# creating button
myButton1=Button(root,text="Click Me!",state=DISABLED,fg="red")
myButton2=Button(root,text="Click Me!",padx=50,pady=50,command=myClick,foreground="blue")
myButton3=Button(root,text="Click Me!",fg="red",bg="#2c95a3")
# state=DISABLED will desabled the state of the button
# padx is for x padding and pady for y padding
# fg or foreground is for forground color
# bg or background is for background color

# packing button
myButton1.pack()
myButton3.pack()
myButton2.pack()
root.mainloop()
