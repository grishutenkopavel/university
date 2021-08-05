from tkinter import *
root=Tk()
root.title('Графические примитивы')
def clickOnButton1():
    x = int(textFild1.get())
    y = int(textFild2.get())
    labelFild.config(text=str(x+y))

button1 = Button(root, text="OK", command=clickOnButton1)
textFild1 = Entry()
textFild2 = Entry()
labelFild = Label()
textFild1.pack()
textFild2.pack()
labelFild.pack()
button1.pack()

root.mainloop()