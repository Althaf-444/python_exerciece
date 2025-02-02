from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("learn tkinter")
root.iconbitmap('c:/Users/RASLAN/Downloads/laptop.png')

img1 = ImageTk.PhotoImage(Image.open("images/3.png"))
img2 = ImageTk.PhotoImage(Image.open("images/4.jfif"))
img3 = ImageTk.PhotoImage(Image.open("images/5.jfif"))
img4 = ImageTk.PhotoImage(Image.open("images/6.jfif"))
img5 = ImageTk.PhotoImage(Image.open("images/7.jfif"))

image_list = [img1,img2,img3,img4,img5]

status = Label(root, text= "Image 1 of " + str(len(image_list)),bd= 1 ,relief=SUNKEN , anchor=E)

my_labal = Label(image=img1)
my_labal.grid(row=0,column=0,columnspan=3)

def right(img_num):
  global my_labal
  global btn_back
  global btn_right
  my_labal.grid_forget()
  my_labal= Label(image=image_list[img_num-1])
  btn_right = Button(root,text=">>",command=lambda: right(img_num+1))
  btn_back = Button(root,text="<<",command=lambda: back(img_num-1))
  
  if img_num == 5:
    btn_right = Button(root ,text=">>" , state=DISABLED)
  
  
  my_labal.grid(row=0,column=0,columnspan=3)
  btn_back.grid(row=1,column=0)
  btn_right.grid(row=1,column=2)

  status = Label(root, text= "Image "+ str(img_num) +" of " + str(len(image_list)),bd= 1 ,relief=SUNKEN , anchor=E)
  status.grid(row=2,column=0,columnspan= 3 , sticky=W+E)




    
def back(img_num):
  global my_labal
  global btn_back
  global btn_right
  my_labal.grid_forget()
  my_labal= Label(image=image_list[img_num-1])
  btn_right = Button(root,text=">>",command=lambda: right(img_num+1))
  btn_back = Button(root,text="<<",command=lambda: back(img_num-1))

  if img_num == 1:
    btn_back = Button(root ,text="<<" , state=DISABLED)
  
  my_labal.grid(row=0,column=0,columnspan=3) 
  btn_back.grid(row=1,column=0)
  btn_right.grid(row=1,column=2)


  status = Label(root, text= "Image "+ str(img_num) +" of " + str(len(image_list)),bd= 1 ,relief=SUNKEN , anchor=E)
  status.grid(row=2,column=0,columnspan= 3 , sticky=W+E)



btn_back = Button(root,text="<<",command=back,state=DISABLED)
btn_exit = Button(root,text="Exit programe", command= root.quit)
btn_right = Button(root,text=">>",command=lambda: right(2))

btn_back.grid(row=1,column=0)
btn_exit.grid(row=1,column=1)
btn_right.grid(row=1,column=2,pady=10)
status.grid(row=2,column=0,columnspan= 3 , sticky=W+E)





root.mainloop()