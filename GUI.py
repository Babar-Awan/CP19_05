from tkinter import *
root = Tk()
root.geometry("1000x600")
root.title("Face Detection In Real Time")
def testing():
    print("TESTING")
def save():
    print ("YOUR DATA IS SAVE")
f1 = Frame(root, bg = "black", borderwidth = 1 , relief = GROOVE)
f1.pack(side = TOP, fill="x")
 
f2 = Frame(root, bg = "black", borderwidth = 5 , relief = GROOVE)
f2.pack(side = BOTTOM, fill="x")




f3 = Frame(root, bg = "black", borderwidth = 1 , relief = GROOVE)
f3.pack(side = TOP, fill="y")


l2 = Label(f1, text = "                FACE DETECTON                  ",bg = "black" , fg = "white" , font = ("Arial",30,"bold"))
l2.pack()
l3 = Label(f2, text = "Teachers:  Sir Asim Imdad,  Sir Adil Rao,  Miss Ishrat Fatima  ", bg = "black", fg="white" , font = ("Arial",10,"bold") )
l3.pack(side=LEFT)
l3 = Label(f2, text = "Members:  Hassan Ali,  Arsalan Ahmed,  Haziq Ahmed,  Babar Awan,  Farooq Arman   ", bg = "black", fg="white" , font = ("Arial",10,"bold") )
l3.pack(side=RIGHT)




B3 = Button(root, text ="DATA SAVE", bg = "Black", fg="white", height = 2, width = 10 ,font = ("Arial",10,"bold"), command=save )
B3.pack(side=RIGHT, anchor="sw", padx=20, pady=20)
B2 = Button(root, text ="CLOSE", bg = "Black", fg="white", height = 2, width = 10 ,font = ("Arial",10,"bold"), command=root.destroy )
B2.pack(side=RIGHT, anchor="sw", padx=20, pady=20)

B1 = Button(root, text ="START", bg = "Black", fg="white", height = 2, width = 10,font = ("Arial",10,"bold"), command=testing  )
B1.pack(side=RIGHT, anchor="sw", padx=20, pady=20)

root.mainloop()
