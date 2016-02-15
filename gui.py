from Tkinter import *
import tkFileDialog
import logic
root=Tk()
e=StringVar();
tx=StringVar();
root.geometry("400x400+200+200")
label = Label( root, text="*.c  or *.cpp formats only").grid(row=0,column=0)

def bro():
    file = tkFileDialog.askopenfile(parent=root,mode='rb',title='Choose a file')
    e.set(file.name)

def calc():
    ty=logic.frr(e.get())
    tx.set(''.join(ty))

    
E1 = Entry(root,textvariable=e).grid(row=1,column=0)
B = Button(root, text ="Browse", command = bro).grid(row=1,column=1)
B1 = Button(root, text ="Calculate",command=calc).grid(row=2,column=1)
label1 = Label( root, textvariable=tx,text="res").grid(row=3,column=0)
label2 = Label( root, text="Developed by Ragul J R").grid(row=4,column=0)
root.mainloop()
