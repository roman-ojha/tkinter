from tkinter import *
root =Tk()



userName=Entry(root,width=50,bg="#a2d5db",fg="black",borderwidth=5)
# here Entry widget of the input field
userName.pack()
userName.insert(0,"Enter Your Name:")
# insert() to put some default value in the text field
def getName():
    name=Label(root,text=userName.get())
    # get() function will get the data from the input field
    name.pack()

submit=Button(root,text="Submit",height=5,width=10,command=getName)
submit.pack()

root.mainloop()
