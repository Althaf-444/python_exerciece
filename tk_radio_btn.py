from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("learn tkinter")
root.iconbitmap('c:/Users/RASLAN/Downloads/laptop.png')




modes =[
 ("peper","peper"),
 ("cheese","cheese"),
 ("mashroom","mashroom"),
 ("onion","onion")
]

pizza = StringVar()
pizza.set('peper')

for text , mode in modes :
  Radiobutton(root,text=text,variable=pizza,value=mode).pack()


def click(value):
  lable1 = Label(root, text= value)
  lable1.pack()

#Radiobutton(root,text="Option 1",variable=r,value=1,command=lambda:click(r.get())).pack()
#Radiobutton(root,text="Option 2",variable=r,value=2,command=lambda:click(r.get())).pack()

# lable = Label(root, text= pizza.get())
# lable.pack()

my_btn = Button(root,text='click me',command=lambda: click(pizza.get()))
my_btn.pack()
root.mainloop()