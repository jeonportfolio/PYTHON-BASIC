
from tkinter import *
from tkinter import messagebox

def clickImage(event) :
    messagebox.showinfo("마우스", "토끼에서 마우스가 클릭됨")

window = Tk()
window.geometry("400x400")

photo = PhotoImage(file = "chapter10/GIF/rabbit.gif")
label1 = Label(window, image = photo)

label1.bind("<Button>", clickImage)

label1.pack( expand = True, anchor = CENTER)
window.mainloop()
