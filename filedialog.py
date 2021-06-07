from tkinter import *
from tkinter import filedialog

root = Tk()

root.filename = filedialog.askopenfilename(initialdir="./", title="Select File", filetypes=(("png files", "*.png"), ("all files", "*.*")))


root.mainloop()
