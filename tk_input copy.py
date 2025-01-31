from tkinter import *

root = Tk()

e= Entry(root,width=50)
e.pack()
e.insert(0,"Enter Your Name: ")

def myclick():
     hello="hello " + e.get()
     mylabal= Label(root, text=hello)
     mylabal.pack()
     

mybtn = Button(root, text="click me",command= myclick,fg="blue").pack()




root.mainloop()