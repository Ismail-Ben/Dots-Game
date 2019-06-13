from tkinter import *

import random

import time

WIDTH = 700

HEIGHT = 400

ENEMY_SIZE = 15
ENEMY_MOVE = 10


class Jeu:
    def __init__(self):
        self.app = Tk()
        self.c = Canvas(self.app, width=WIDTH, height=HEIGHT, bg="grey")
        self.app.resizable(False, False)
        self.c.pack()
        self.generator = EnemyGenerator()
        self.enemies = []

        for i in range(50):
            enemy = self.generator.generate(self.c)
            self.enemies.append(enemy)

        self.update()
        self.app.mainloop()

    def update(self):
        for enemy in self.enemies:
            enemy.update()

        self.app.after(50, self.update)


class Enemy:

    def __init__(self):

        self.c = None

        self.side = 0

        self.move = (0, 0)

        self.obj = None

    def update(self):
        x, y = self.c.coords(self.obj)[:2]
        x_actuel = x
        y_actuel = y

        x += self.move[0]
        y += self.move[1]
        if x >= WIDTH - ENEMY_SIZE:
            self.move = (self.move[0] * -1, self.move[1])
        elif x <= 0:
            self.move = (self.move[0]*-1,self.move[1])
        if y >= HEIGHT - ENEMY_SIZE:
            self.move = (self.move[0] , self.move[1]*-1)
        elif y <= 0:
            self.move = (self.move[0] , self.move[1]*-1)

        self.c.move(self.obj, x - x_actuel, y - y_actuel)


class EnemyGenerator:

    def __init__(self):

        # 0 = top, 1 = right, 2 = bottom, 3 = left
        self.side = 0

    def generate(self, c):
        enemy = Enemy()
        enemy.side = self.side
        enemy.c = c

        if self.side == 0:
            # top
            xo = random.randint(0, WIDTH - ENEMY_SIZE)
            enemy.obj = c.create_oval(xo, 0, xo + ENEMY_SIZE, ENEMY_SIZE, fill='red')
            enemy.move = (0, ENEMY_MOVE)
        elif self.side == 1:
            # right
            yo = random.randint(0, HEIGHT - ENEMY_SIZE)
            enemy.obj = c.create_oval(WIDTH - ENEMY_SIZE, yo, WIDTH, yo + ENEMY_SIZE, fill='red')
            enemy.move = (-ENEMY_MOVE, 0)
        elif self.side == 2:
            # bottom
            xo = random.randint(0, WIDTH - ENEMY_SIZE)
            enemy.obj = c.create_oval(xo, HEIGHT - ENEMY_SIZE, xo + ENEMY_SIZE, HEIGHT, fill='red')
            enemy.move = (0, -ENEMY_MOVE)
        else:
            # left
            yo = random.randint(0, HEIGHT - ENEMY_SIZE)
            enemy.obj = c.create_oval(0, yo, ENEMY_SIZE, yo + ENEMY_SIZE, fill='red')
            enemy.move = (ENEMY_MOVE, 0)

        self.side = (self.side + 1) % 4

        return enemy


Jeu()

"""root = Tk()

root.resizable(False, False)

c = Canvas(root, width=WIDTH, height=HEIGHT, bg='grey')

c.pack()

a = enemy_generator()

a.horizontal_enemy_generator()"""

a.horizontal_enemy_generator()

root.mainloop()
