from tkinter import *
import pygame

pygame.init
gui = Tk()
gui.title("IN BETWEEN")
gui.geometry("640x360")
gui.resizable(FALSE, FALSE)

global count

count=0

def start():

    global count
    count +=1


button = Button(gui, text="start", command=start)
button.pack()

print(count)

gui.mainloop()