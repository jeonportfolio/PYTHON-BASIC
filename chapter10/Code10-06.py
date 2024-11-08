from tkinter import *
from tkinter import messagebox

def myFunc() : 
    messagebox.showinfo("강아지버튼", "강아지가 귀엽죠?^^")

window =Tk()

photo = PhotoImage(file="chapter10/GIF/dog2.gif")
button1 = Button(window, image = photo, command=myFunc)

button1.pack()

window.mainloop()

