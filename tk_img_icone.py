from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("learn tkinter")
root.iconbitmap('c:/Users/RASLAN/Downloads/laptop.png')

img1 = ImageTk.PhotoImage(Image.open("images/1.jpeg"))
my_labal = Label(image=img1)
my_labal.pack()




ex_btn = Button(root, text="Exit Program" , command= root.quit)
ex_btn.pack()



root.mainloop()