#!/usr/bin/env python3
from tkinter import *

root = Tk()

def print1(event):
  print("1")

def print2(event):
  print("2")


btn1 = Button(root,                  
             text="Закрыть",       
             width=30,height=5,     
             bg="white",fg="black")
btn1.bind("<Button-1>", exit)      
btn1.pack()  

btn2 = Button(root, text="1")
btn2.bind("<Button-1>", print1)       
btn2.pack(side = 'right')   

btn3 = Button(root, text="2") 
btn3.bind("<Button-1>", print2)    
btn3.pack(side = 'left')   

def main():
  root.mainloop()
