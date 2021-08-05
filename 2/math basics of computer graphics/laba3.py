from tkinter import *

root = Tk()
root.title('График функции')
frameA = Frame(root)
frameA.pack()
frameB = Frame(root)
frameB.pack()
frameC = Frame(root)
frameC.pack()
frameMin = Frame(root)
frameMin.pack()
frameMax = Frame(root)
frameMax.pack()
canvframe = Frame(root)
canvframe.pack()

w = 500
h = 500

labelA = Label(frameA, text="a")
labelA.pack(side = LEFT)
entryA = Entry(frameA)
entryA.pack(side = LEFT)

labelB = Label(frameB, text="b")
labelB.pack(side = LEFT)
entryB = Entry(frameB)
entryB.pack(side = LEFT)

labelC = Label(frameC, text="c")
labelC.pack(side = LEFT)
entryC = Entry(frameC)
entryC.pack(side = LEFT)

labelMin = Label(frameMin, text="Xmin Ymin")
labelMin.pack(side = LEFT)
entryMin = Entry(frameMin)
entryMin.pack(side = LEFT)

labelMax = Label(frameMax, text="Xmax Ymax")
labelMax.pack(side = LEFT)
entryMax = Entry(frameMax)
entryMax.pack(side = LEFT)

def clickOnButton1():
    canv.delete("all")
    maxs = entryMax.get().split()
    mins = entryMin.get().split()
    xmin = int(mins[0])
    ymin = int(mins[1])
    xmax = int(maxs[0])
    ymax = int(maxs[1])
    a = int(entryA.get())
    b = int(entryB.get())
    c = int(entryC.get())
    
    canv.create_line(0, h/2-1, w, h/2-1) #ось x 
    canv.create_line(w/2-1, 0, w/2-1, h) #ось y

    x0 = xmin
    y0 = a*x0*x0+b*x0*c
    y = 0
    x = xmin
    while x0 < xmax:
        x = x + 1
        y = a*x*x+b*x+c
        xk0 = round(x0+w/2)
        yk0 = round(h/2-y0)
        yk = round(h/2-y)
        xk = round(x+w/2)
        canv.create_line(xk0, yk0, xk, yk)
        x0 = x
        y0 = y
    

button1 = Button(canvframe, text="OK", command=clickOnButton1)
button1.pack(side = TOP)

canv=Canvas(canvframe,width=w,height=h,bg="white")
canv.pack(side = BOTTOM)


root.mainloop()