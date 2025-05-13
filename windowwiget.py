from tkinter import *

btnlist=[None]*9
fnameList=["an3.gif","a0.gif","a.gif","an4.gif","an5.gif","an6.gif","an7.gif","an8.gif","an9.gif"]
photoList=[None]*9
i,k=0,0
xPos,yPos=0,0
num=0

window=Tk()
window.geometry("210x210")

for i in range(0,9):
    photoList[i]=PhotoImage(file="C:\\Users\\사용자\\Downloads\\windowprogram\\"+fnameList[i])
    btnlist[i]=Button(window,image= photoList[i])

for i in range(0,3):
    for k in range(0,3):
        btnlist[num].place(x=xPos, y=yPos)
        num+=1
        xPos=70
    xPos=0
    yPos+=70

window.mainloop()

