from tkinter import *
import random
import time

WIDTH = 700
HEIGHT = 400
ENEMY_SIZE = 15


class enemy_generator:
    def __init__(self):
        self.sidex = True
        self.sidey = True
        self.movex = True
        self.movey = True

    def horizontal_enemy_generator(self):
        yo = random.randint(0, HEIGHT - ENEMY_SIZE)
        if self.sidex:

            enemy = c.create_oval(0, yo, ENEMY_SIZE, yo + ENEMY_SIZE, fill='red')
        else:

            enemy = c.create_oval(WIDTH - ENEMY_SIZE, yo, WIDTH, yo + ENEMY_SIZE, fill='red')
        self.enemy_movement_x(enemy)
        self.sidex = not self.sidex

    def vertical_enemy_generator(self):

        xo = random.randint(0, WIDTH - ENEMY_SIZE)
        if self.sidey:
            enemy = c.create_oval(xo, 0, xo + ENEMY_SIZE, ENEMY_SIZE, fill='red')
        else:
            enemy = c.create_oval(xo, HEIGHT - ENEMY_SIZE, xo + ENEMY_SIZE, HEIGHT, fill='red')
        self.enemy_movement_y(enemy)
        self.sidey = not self.sidey

    def enemy_movement_x(self, enemy):
        print(c.coords(enemy)[0])

        if c.coords(enemy)[0] >= WIDTH - ENEMY_SIZE:
            self.movex = False
        if c.coords(enemy)[0] <= 0:
            self.movex = True

        if self.movex:
            c.move(enemy, 10, 0)
            c.update()
            c.after(50, self.enemy_movement_x, enemy)
        if not self.movex:
            c.move(enemy, -10, 0)
            c.update()
            c.after(50, self.enemy_movement_x, enemy)

    def enemy_movement_y(self):
        pass


root = Tk()
root.resizable(False, False)
c = Canvas(root, width=WIDTH, height=HEIGHT, bg='grey')
c.pack()
a = enemy_generator()
a.horizontal_enemy_generator()

a.horizontal_enemy_generator()
root.mainloop()
