from tkinter import *
import math
root=Tk()
root.title('N - угольник')
def clickOnButton1():
    canv.delete("all")
    n = int(textFild1.get())
    if n > 2:
        r = 100
        pi = 3.141592
        x0 = 250 - 1
        y0 = 250 - 1
        x1 = x0+r*math.cos((2*pi*0)/n)
        y1 = y0+r*math.sin((2*pi*0)/n)
        for i in range(n):
            x = x0+r*math.cos((2*pi*(i+1))/n)
            y = y0+r*math.sin((2*pi*(i+1))/n)
            canv.create_line(round(x1), round(y1), round(x), round(y))
            x1 = x
            y1 = y

    else:
        pass

button1 = Button(root, text="OK", command=clickOnButton1)

textFild1 = Entry()
labelHelp = Label(text="Введите количество углов")
labelHelp.pack()
textFild1.pack()
button1.pack()
canv=Canvas(root,width=500,height=500,bg="white")


canv.pack()
root.mainloop()