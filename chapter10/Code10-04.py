from tkinter import *
window = Tk()

photo = PhotoImage(file="chapter10/GIF/dog.gif")
label1 = Label(window, image = photo)

label1.pack()

window.mainloop()
