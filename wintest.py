from tkinter import *

window=Tk()
window.title("윈도우창 연습")
window.geometry("400x100")
window.resizable(width=TRUE,height=FALSE)

label1=Label(window,text="cookbook~~~python을")
label2=Label(window,text="열심히",font =("궁서체",30),fg="blue")
label3=Label(window,text="공부중입니다.", bg="magenta", width=20, height=5, anchor =SE)

label1.pack()
label2.pack()
label3.pack()

window.mainloop()