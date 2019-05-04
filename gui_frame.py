### Libraries ###
import tkinter as tk
from tkinter import messagebox
from tkinter import Frame
from tkinter import StringVar
from tkinter import *


root = tk.Tk()
form = Frame(root)
form.grid()

### Size ###
root.geometry("260x500")
root.title("GUI")

tv1 = StringVar()

### Fuctions ###
def helloCallBack():
    messagebox.showinfo("how's ur frame" , tv1.get())
    tv1.get("ok")
    
def helloCallBack2():
    messagebox.showinfo("welcome" , "How are u programers??")


### Label ###
L1 = tk.Label(form,text = "Heading")
L1.grid(row=2,column=2,padx=60, pady = 60)
    
### Buttons ###    
B1 = tk.Button(form, text="DONE", height = 5, width = 10 , bg = "blue" , fg = "white", command = helloCallBack)
B1.grid(row=3,column=1,padx=30, pady = 30)

B2 = tk.Button(form, text="DONE", height = 5, width = 10 , bg = "grey" , fg = "Black", command = helloCallBack2)
B2.grid(row=4,column=1,padx=30, pady = 30)

### Input ###
t1 = tk.Entry (form, textvariable = tv1)
t1.grid (row = 2 , column = 1)




#B1.pack()
#B2.pack()
#L1.pack()

root.mainloop()