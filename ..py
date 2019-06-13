from tkinter import *
import time
import pygame

from random import randint

class enemies:
    def __init__(self):

        pass
root = Tk()

def food_generator(x):
    xi = randint(0,width-10)
    yi = randint(0, height-10)
    food = c.create_oval(xi,yi,xi+10,yi+10, fill = 'blue')
    c.update()
def horizontal_dot_generator(x):
    a=True
    xi= 0
    yi=randint(0,height-20)

    obj=c.create_oval(xi, yi, xi+20, yi+20, fill ='red')
    mouvementx(obj, xi, a)
    food_generator(1)
    generate.bind('<Button-1>', vertical_dot_generator)
def vertical_dot_generator(y):
    b = True
    xi = randint(0,width-20)
    yi =0
    obj=c.create_oval(xi, yi, xi+20, yi+20, fill ='red')
    mouvementy(obj,yi,b)
    food_generator(1)
    generate.bind('<Button-1>', horizontal_dot_generator)
def mouvementx(obj, x, a):
    global  c

    if (x == width-20):
        a = False
    if (x == 0):
        a = True
    if a == True:
        c.move(obj, 10, 0)

        x+=10
    if a==False:
        c.move(obj, -10, 0)
        x-=10
    #time.sleep(0.001)
    c.update()
    root.after(50, mouvementx, obj, x, a)

def mouvementy(obj,y,b):
    global c
    if (y == height-20):
        b = False
    if (y == 0):
        b = True
    if b == True:

        c.move(obj,0,10)
        y+=10
    if b== False:
        c.move(obj,0, -10)
        y-=10
    c.update()
    root.after(50, mouvementy,obj,y,b)

def moveup(event):

    global c ,  character
    ypos = (c.coords(character)[1])
    if 0<= ypos:
        c.move(character,0,-5)

    c.update()

def movedown(event):
    global c ,  character
    ypos = (c.coords(character)[1])
    if ypos <= 365:
        c.move(character,0,5)
    c.update()

def moveleft(event):
    global c, character
    xpos = (c.coords(character)[0])
    if xpos < 0:
        xpos+=10
    if 0<=xpos:
        c.move(character,-5,0)

    c.update()

def moveright(event):
    global c, character
    xpos = (c.coords(character)[0])
    if xpos >665 :
        xpos-=10
    if xpos<=665:
        c.move(character,5,0)

    c.update()

width = 700
height = 400
c = Canvas(root, width= width, height = height, bg = "grey")
character = c.create_oval(width/2,height/2,width/2+35,height/2+35, fill = 'yellow')

ypos = (c.coords(character)[1])

generate = Button(c, text= 'Generate')
generate.place(x=340, y = 360)
compteur = 0
generate.bind('<Button-1>', horizontal_dot_generator)

print(c.coords(character)[0])
#generate_window=c.create_window(10,10,anchor = NE, window=generate)
c.pack()
root.bind('<Left>', moveleft )
root.bind('<Right>', moveright )
root.bind('<Up>',moveup )
root.bind('<Down>', movedown)
root.resizable(width=False, height = False)










#root.after_idle(mouvement)
root.mainloop()
