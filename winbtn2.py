from tkinter import *
from tkinter import messagebox

def myFunc():
    messagebox.showinfo("안 버튼","아이돌입니다")

window=Tk()

photo=PhotoImage(file="C:\\Users\\사용자\\Downloads\\windowprogram\\yujin.gif")
button1=Button(window, image=photo, command=myFunc)

button1.pack()


window.mainloop()