import cv2
import numpy as np
import dlib
from tkinter import *
import sys
import time
from PIL import Image, ImageTk

cap = cv2.VideoCapture(0)
detector = dlib.get_frontal_face_detector()

root = Tk()
#root.geometry("975x585")
root.attributes("-fullscreen", True)
root.title("Face Detection In Real Time")
def testing():
    print("TESTING")
def save():
    print ("YOUR DATA IS SAVE")
###------------ FRAME --------###
f1 = Frame(root, bg = "black", borderwidth = 1 , relief = GROOVE)
f1.pack(side = TOP, fill="x")
 
f2 = Frame(root, bg = "black", borderwidth = 5 , relief = GROOVE)
f2.pack(side = BOTTOM, fill="x")
### FUNCTION ###
def tick():
    time_string = time.strftime("%H:%M:%S")
    clock.config(text=time_string)
    fd()
    clock.after(200, tick)
## USE FOR VIDEO FRAME AND CAPTURE#######    
    
def fd():

    ret,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=detector(gray)
    for face in faces:
        x,y=face.left(),face.top()
        w,h=face.right(),face.bottom()
        cv2.rectangle(frame,(x,y),(w,h),(0,225,0),3)
    im1 = Image.fromarray(frame)     
    photo_root = ImageTk.PhotoImage(im1)
    img_root.config(image = photo_root)
    img_root.image = photo_root

img_root = Label(root, text = "Live Streaming" , font = ("Arial",30,"bold"))
img_root.pack()



## VIDEO detection 
f3 = Frame(root, bg = "black", borderwidth = 1 , relief = GROOVE )
f3.pack(side = TOP, fill="y")

## HEADER ##
l2 = Label(f1, text = "                FACE DETECTON                  ",bg = "black" , fg = "white" , font = ("Arial",30,"bold"))
l2.pack()
## FOOTER ##
l3 = Label(f2, text = "Teachers:  Sir Asim Imdad,  Sir Adil Rao,  Miss Ishrat Fatima  ", bg = "black", fg="white" , font = ("Arial",10,"bold") )
l3.pack(side=LEFT)
l3 = Label(f2, text = "Members:  Hassan Ali,  Arsalan Ahmed,  Haziq Ahmed,  Babar Awan,  Farooq Arman   ", bg = "black", fg="white" , font = ("Arial",10,"bold") )
l3.pack(side=RIGHT)


clock=Label(f3, font=("times", 10, "bold"), fg="green", bg="silver")
clock.pack(anchor=S,side=BOTTOM )
## BUTTONS   ##
B3 = Button(root, text ="DATA SAVE", bg = "Black", fg="white", height = 2, width = 10 ,font = ("Arial",10,"bold"), command=save )
B3.pack(side=RIGHT, anchor="sw", padx=20, pady=20)
B2 = Button(root, text ="CLOSE", bg = "Black", fg="white", height = 2, width = 10 ,font = ("Arial",10,"bold"), command=root.destroy )
B2.pack(side=RIGHT, anchor="sw", padx=20, pady=20)

B1 = Button(root, text ="START", bg = "Black", fg="white", height = 2, width = 10,font = ("Arial",10,"bold"), command=tick  )
B1.pack(side=RIGHT, anchor="sw", padx=0, pady=20)

root.mainloop()
cap.release()
