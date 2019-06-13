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
        self.c = Canvas(self.app,width=WIDTH,height=HEIGHT, bg="grey")
        self.app.resizable(False,False)
        self.c.pack()
        self.generator = EnemyGenerator()
        self.enemies = []

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

        self.side = 0

        self.move = (0, 0)

        self.obj = None

    def update(self):
        pass

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

class EnemyGenerator:

    def __init__(self):

        # 0 = top, 1 = right, 2 = bottom, 3 = left
        self.side = 0

    def generate(self, c):
        enemy = Enemy()
        enemy.side = self.side

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