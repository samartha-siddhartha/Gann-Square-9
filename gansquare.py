from Tkinter import *
from app5 import GannY,GannX,PartA,PartB,Compare
root = Tk()

def OnStart():
    for i in range(1,8):

        for j in range(1,8):
            e = Entry(root,relief=RIDGE,bg='white')
            e.grid(row=i, column=j, sticky=NSEW)
            e.insert(END, ' ')

f = Entry(root,relief=RIDGE)
f.grid(row=0,column=4)
# k = Entry(root,relief=RIDGE)
# k.grid(row=0,column=3)
def OnPress():
    OnStart()
    number =int(f.get())
    # prevclose =int(k.get())
    # number =close-(close-prevclose)
    data1 =GannY(number)
    data2 =GannX(number)
    data3=PartA(number)
    data4=PartB(number)
    a=1
    b=7
    for d,s,x,l in zip(data1,data2,data3,data4):
        d=str(d)
        s=str(s)
        x=str(x)
        l=str(l)

        m=Entry(root,relief=RIDGE,bg='green')
        m.grid(row=a, column=b)
        m.insert(END, l)

        h=Entry(root,relief=RIDGE,bg='green')
        h.grid(row=a, column=a)
        h.insert(END, x)

        g =Entry(root,relief=RIDGE,bg='yellow')
        g.grid(row=4, column=a)
        g.insert(END, s)

        e=Entry(root,relief=RIDGE,bg='red')
        e.grid(row=a, column=4)
        e.insert(END, d)

        a+=1
        b-=1
    #root2=Tk()
    gann =Entry(root,relief=RIDGE,bg='blue')
    position = Compare(number)
    gann.grid(row=position[0],column=position[1])
    gann.insert(END,number)
    a=1
    print position[2],position[3]
    for by in position[2]:
        buy = Entry(root, relief=RIDGE, bg='green', fg='white')
        buy.grid(row=20, column=a)
        buy.insert(END, by)
        a += 1
    a=1
    for se in position[3]:
        sell = Entry(root, relief=RIDGE, bg='red', fg='white')
        sell.grid(row=22, column=a)
        sell.insert(END, se)
        a += 1






OnStart()

Button(root,text='Gann Square 9', command=OnPress).grid(row =0,column=5)
Button(root,text='Refresh', command=OnStart).grid(row =0,column=1)





mainloop()

#