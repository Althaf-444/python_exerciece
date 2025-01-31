from tkinter import *

root = Tk()

def myclick():
     mylabal= Label(root, text='look i crate btn!',fg='red')
     mylabal.pack()
     

mybtn = Button(root, text="click me",command= myclick,fg="blue",bg='#000000').pack()




root.mainloop()