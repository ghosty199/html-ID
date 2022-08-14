from tkinter import *
import random
from PIL import Image, ImageTk
root=Tk()
root.minsize(650,650)
root.maxsize(650,650)
root.title("html ID")
root.config(bg="white")
save1=ImageTk.PhotoImage(Image.open("save.png"))
open1=ImageTk.PhotoImage(Image.open("open.png"))
play1=ImageTk.PhotoImage(Image.open("play.png"))




label5=Label(root,text="File name", bg="white", fg="black")
label5.place(relx=0.4, rely=0.1, anchor=CENTER)

inputbox=Entry(root,)
inputbox.place(relx=0.6, rely=0.1, anchor=CENTER)

my_text=Text(root,height=35, width=80)
my_text.place(relx=0.5, rely=0.55, anchor=CENTER)




button1=Button(root,image=save1)
button1.place(relx=0.1, rely=0.1, anchor=CENTER)

button2=Button(root,image=open1)
button2.place(relx=0.2, rely=0.1, anchor=CENTER)

button3=Button(root,image=play1)
button3.place(relx=0.3, rely=0.1, anchor=CENTER)



































root.mainloop()