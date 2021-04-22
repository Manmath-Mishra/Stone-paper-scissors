from tkinter import *
import random
import tkinter.messagebox
score=0
scorec=0
def stone():
    Choices=["Stone","Paper","Scissor"]
    a= random.choice(Choices)
    hs.set("Stone")
    root.update()
    cs.set(a)
    root.update()
    global score
    global scorec
    if a=="Stone":
        hs1.set("TIE")
        cs1.set("TIE")
        root.update()
    if a=="Paper":
        scorec+=1
        hs1.set(score)
        cs1.set(scorec)
        root.update()
    if a=="Scissor":
        score+=1
        hs1.set(score)
        cs1.set(scorec)
        root.update()
    if score==5 and scorec<5:
        hs1.set(f"{name} won!!!")
        cs1.set("Computer lost")
        root.update()
        tkinter.messagebox.showinfo("Result",f"{name} won!!")
        root.destroy()
    if scorec==5 and score<5:
        hs1.set(f"{name} lost")
        cs1.set("Computer won!!!")
        root.update()
        tkinter.messagebox.showinfo("Result","Computer won!!")
        root.destroy()
def paper():
    Choices=["Stone","Paper","Scissor"]
    a= random.choice(Choices)
    hs.set("Paper")
    root.update()
    cs.set(a)
    root.update()
    global score
    global scorec
    if a=="Stone":
        score+=1
        hs1.set(score)
        cs1.set(scorec)
        root.update()
    if a=="Paper":
        hs1.set("TIE")
        cs1.set("TIE")
        root.update()
    if a=="Scissor":
        scorec+=1
        hs1.set(score)
        cs1.set(scorec)
        root.update()
    if score==5 and scorec<5:
        hs1.set(f"{name} won!!!")
        cs1.set("Computer lost")
        root.update()
        tkinter.messagebox.showinfo("Result",f"{name} won!!")
        root.destroy()
    if scorec==5 and score<5:
        hs1.set(f"{name} lost")
        cs1.set("Computer won!!!")
        root.update()
        tkinter.messagebox.showinfo("Result","Computer won!!")
        root.destroy()
def scissor():
    Choices=["Stone","Paper","Scissor"]
    a= random.choice(Choices)
    hs.set("Scissor")
    root.update()
    cs.set(a)
    root.update()
    global score
    global scorec
    if a=="Stone":
        scorec+=1
        hs1.set(score)
        cs1.set(scorec)
        root.update()
    if a=="Paper":
        score+=1
        hs1.set(score)
        cs1.set(scorec)
        root.update()
    if a=="Scissor":
        hs1.set("TIE")
        cs1.set("TIE")
        root.update()
    if score==5 and scorec<5:
        hs1.set(f"{name} won!!!")
        cs1.set("Computer lost")
        root.update()
        tkinter.messagebox.showinfo("Result",f"{name} won!!")
        root.destroy()
    if scorec==5 and score<5:
        hs1.set(f"{name} lost")
        cs1.set("Computer won!!!")
        root.update()
        tkinter.messagebox.showinfo("Result","Computer won!!")
        root.destroy()
name= input("PLEASE ENTER PLAYER NAME :")
root=Tk()
root.configure(bg="grey")
root.title("Stone Paper Scissors")
root.geometry("600x500")
root.resizable(0,0)
f=Frame(root,bg="red")
l= Label(f,text="Stone Paper Scissors",justify='center',font='algerian 20 bold')
f.pack(side=TOP,fill=BOTH)
l10= Label(f,text="The first to score 5 wins",justify='center',font='algerian 15',bg="light blue")
l.pack()
l10.pack()
f2= Frame(root)
l1= Label(f2,text=f"{name} options:",font='algerian 15')
f2.pack(side=LEFT)
f2.place(y=100)
l1.pack()
f3=Frame(root)
b= Button(f3,text="Stone",bg="light green",padx=40,pady=5,command=stone)
b1= Button(f3,text="Paper",bg="light green",padx=40,pady=5,command=paper)
b2= Button(f3,text="Scissor",bg="light green",padx=40,pady=5,command=scissor)
f3.pack()
f3.place(x=100,y=170)
b.pack(side=LEFT,ipadx=5)
b1.pack(side=LEFT,ipadx=5)
b2.pack(side=LEFT,ipadx=5)
f4=Frame(root)
f5=Frame(root)
l3=Label(f4,text=f"{name} choice :",font="lucida 15")
l4= Label(f5,text="Computer choice :",pady=20,font="lucida 15")
f4.pack(fill=BOTH)
f4.place(x=30,y=250,width=500,height=100)
l3.pack()
l3.place(x=30)
f5.pack()
f5.place(x=30,y=280,width=500)
l4.pack(side=LEFT)
hs= StringVar()
cs= StringVar()
hscore= Entry(f4,textvariable=hs,font="lucida 15")
cscore= Entry(f5,textvariable=cs,font="lucida 15")
hscore.pack()
hscore.place(x= 240)
cscore.pack()
cscore.place(x=240,y=15)
hs1= StringVar()
cs1 = StringVar()
f6= Frame(root)
f7= Frame(root)
l5= Label(f6,text=f"{name} Score:",font="lucida 15")
l6= Label(f7,text="Computer Score:",font="lucida 15")
human= Entry(f6,textvariable=hs1,font="lucida 15")
computer= Entry(f7,textvariable=cs1,font="lucida 15")
f6.pack()
f6.place(x=30,y=380,width=500)
l5.pack(side=LEFT)
human.pack()
human.place(x=240)
f7.pack()
f7.place(x=30,y=420,width=500,height=30)
l6.pack(side=LEFT)
computer.pack()
computer.place(x=240)
root.mainloop()