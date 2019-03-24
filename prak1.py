#!/usr/bin/env python3
from tkinter import *

root = Tk()

btn = Button(root, text="Закрыть") 

btn.bind("<Button-1>", exit)       
btn.pack()                

def main():
  root.mainloop()

if __name__ == '__main__':
    main()