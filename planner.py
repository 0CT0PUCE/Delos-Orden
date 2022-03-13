from tkinter import *
import random

def Convert(string):
    li = list(string.split(" "))
    return li
window = Tk()

window.title("Planner")
window.geometry('1200x450')
lbl0= Label(window, text="")
lbl0.grid(column=0, row=0)

lbl1 = Label(window, text="First class :")
lbl1.grid(column=0, row=1)
txt1 = Entry(window,width=22)
txt1.grid(column=1, row=1)
spin1 = Spinbox(window, from_=1, to=7, width=3)
spin1.grid(column=2,row=1)

lbl2 = Label(window, text="Second class :")
lbl2.grid(column=0, row=2)
txt2 = Entry(window,width=22)
txt2.grid(column=1, row=2)
spin2 = Spinbox(window, from_=1, to=7, width=3)
spin2.grid(column=2,row=2)

lbl3 = Label(window, text="Third class :")
lbl3.grid(column=0, row=3)
txt3 = Entry(window,width=22)
txt3.grid(column=1, row=3)
spin3 = Spinbox(window, from_=1, to=7, width=3)
spin3.grid(column=2,row=3)

lbl4 = Label(window, text="Fourth class :")
lbl4.grid(column=0, row=4)
txt4 = Entry(window,width=22)
txt4.grid(column=1, row=4)
spin4 = Spinbox(window, from_=1, to=7, width=3)
spin4.grid(column=2,row=4)

lbl5 = Label(window, text="Fifth class :")
lbl5.grid(column=0, row=5)
txt5 = Entry(window,width=22)
txt5.grid(column=1, row=5)
spin5 = Spinbox(window, from_=1, to=7, width=3)
spin5.grid(column=2,row=5)

lbl6 = Label(window, text="Weeks of work")
lbl6.grid(column=0, row=6)
spin6 = Spinbox(window, from_=1, to=64, width=3)
spin6.grid(column=2,row=6)

lbl7 = Label(window, text="result")
lbl7.grid(column=0, row=7)

def clicked():
    weeks=spin6.get()
    weeks=int(weeks)
    lbl7.configure(text=("Sucessfully selected your class for",spin6.get(),"weeks"))
    print(txt1.get(), spin1.get())
    i=0
    week=["","","","","","",""]
    days=["monday :","tuesday :","wednesday :","thursday :","friday :","saturday :","sunday :"]
    oldweek=[]
    class1=txt1.get()
    freq1=int(spin1.get())
    class2=txt2.get()
    freq2=int(spin2.get())
    class3=txt3.get()
    freq3=int(spin3.get())
    class4=txt4.get()
    freq4=int(spin4.get())
    class5=txt5.get()
    freq5=int(spin5.get())
    whrow=7
    while i < weeks:
        i=i+1
        bfreq1=freq1
        bfreq2=freq2
        bfreq3=freq3
        bfreq4=freq4
        bfreq5=freq5
        for k in range(7):
            print(k)
            nbm=random.randrange(0, 7, 1)
            if nbm in oldweek:
                while nbm in oldweek:
                    print("class was already there")
                    nbm=random.randrange(0, 7, 1)
            day=days[nbm]
            oldweek.append(nbm)
            print(oldweek)
            print(day)
            day=str(day)
            crday=day
            if bfreq1>0:
                crday=crday+" "+class1
                bfreq1=bfreq1-1
            if bfreq2>0:
                crday=crday+" "+class2
                bfreq2=bfreq2-1
            if bfreq3>0:
                crday=crday+" "+class3
                bfreq3=bfreq3-1
            if bfreq4>0:
                crday=crday+" "+class4
                bfreq4=bfreq4-1
            if bfreq5>0:
                crday=crday+" "+class5
                bfreq5=bfreq5-1
            print(crday)
            Convert(crday)
            print("current day JJJJJJJJJJJJ:",crday)
            week[nbm]=crday
        oldweek=[]
        crday="finished"
        print(week)
        week1 = Label(window, text=week)
        whrow=whrow+1
        week1.grid(column=0, row=whrow)




btn = Button(window, text="Create planning !", command=clicked)

btn.grid(column=1, row=7)

window.mainloop()
