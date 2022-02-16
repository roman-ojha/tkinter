from tkinter import *
root=Tk()
myLabel1=Label(root,text="Hello World")
myLabel2=Label(root,text="My Name is Hohn Elder")
myLabel3=Label(root,text="           ")

myLabel1.grid(row=0,column=0)
myLabel2.grid(row=1,column=5)
myLabel3.grid(row=1,column=1)
# here we are putting the Label widget in the grid according the row and column
# and grid are relative to each other
# or python is object oriented programm so you can also do this
myLabel4=Label(root,text="Hello another world").grid(row=3,column=3)

root.mainloop()