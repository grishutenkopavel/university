from tkinter import *
root=Tk()
root.title('Треугольник')
def clickOnButton1():
    canv.delete("all")
    xylist1 = textFild1.get().split()
    x1 = int(xylist1[0])
    y1 = int(xylist1[1])
    x2 = int(xylist1[2])
    y2 = int(xylist1[3])
    x3 = int(xylist1[4])
    y3 = int(xylist1[5])
    canv.create_line(x1, y1, x2, y2, fill='blue')
    canv.create_line(x2, y2, x3, y3, fill='black')
    canv.create_line(x1, y1, x3, y3, fill='red')

button1 = Button(root, text="OK", command=clickOnButton1)

textFild1 = Entry()
labelHelp = Label(text="Перечислите координаты x1 y1 x2 y2 x3 y3")
labelHelp.pack()
textFild1.pack()
button1.pack()
canv=Canvas(root,width=500,height=500,bg="white")


canv.pack()
root.mainloop()