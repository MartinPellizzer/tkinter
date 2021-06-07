from tkinter import *

root = Tk()

r = IntVar()
r.set("2")

MODES = [
	
]

def clicked(value):
	label = Label(root, text=value)
	label.pack()
	

Radiobutton(root, text="Option 1", variable=r, value=1, command=lambda:clicked(r.get())).pack()
Radiobutton(root, text="Option 2", variable=r, value=2, command=lambda:clicked(r.get())).pack()



label = Label(root, text=r.get())
label.pack()

mainloop()
