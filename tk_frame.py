from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("learn tkinter")
root.iconbitmap('c:/Users/RASLAN/Downloads/laptop.png')

frame= LabelFrame(root,padx=50,pady=50)
frame.pack(padx=10,pady=10)

b=Button(frame, text="Don't click here!")
b.grid(row=0,column=0)




root.mainloop()