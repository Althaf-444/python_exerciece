from tkinter import * 
from PIL import ImageTk,Image
from tkinter import messagebox

root = Tk()
root.title("learn tkinter")
root.iconbitmap('c:/Users/RASLAN/Downloads/laptop.png')

# defferent messageboxes
# showinfo, showwarning , showerror, askquestion, askokcencel, askyesno


def popup():
   responce=messagebox.askyesno("this is my popup","Hello,World!")
#    Label(root,text=responce).pack()
   if responce == 1 :
    Label(root,text="you click yes").pack()
   else:
    Label(root,text="you click no").pack()
      
      



Button(root,text = "popup",command=popup).pack()





root.mainloop()