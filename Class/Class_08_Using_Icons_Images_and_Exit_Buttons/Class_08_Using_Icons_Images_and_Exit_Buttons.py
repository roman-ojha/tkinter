from tkinter import *
from PIL import ImageTk,Image
# pip install Pillow

root=Tk()
root.title("Icons")
# iconbitmap is for the icon that come at the left top side ot the icons
root.iconbitmap('E:\Programming\Python\Tkinter\Class\Class_08_Using_Icons_Images_and_Exit_Buttons\Icons.ico')

my_img=ImageTk.PhotoImage(Image.open("E:\Programming\Python\Tkinter\Class\Class_08_Using_Icons_Images_and_Exit_Buttons\Image.jpg"))
# here we can import or open the image like this 
my_label=Label(image=my_img)
# we we have to put that into widget
my_label.pack()



button_quit=Button(root,text="Exit Program",command=root.quit)
# 'root.quit' to quite the program
button_quit.pack()

root.mainloop()