import pygame
import random
import math

WIDTH = 700

HEIGHT = 400
FOOD_SIZE= 5
ENEMY_SIZE = 11
PLAYER_SIZE = 20
ENEMY_MOVE = 10
RED = (220, 20, 60)
ORANGE= (238,118,0)
PLAYER_MOVE = 20
PINK = (255,105,180)
class Jeu:
    def __init__(self):
        self.app = pygame.display.set_mode((WIDTH, HEIGHT), )
        pygame.display.set_caption('Dots')
        self.joueur= Joueur(self.app)
        self.generator = EnemyGenerator()
        self.enemies = []
        self.food = Food(self.app)
        for i in range(10):
            enemy = self.generator.generate(self.app)
            self.enemies.append(enemy)
        run = True
        while run:
            pygame.time.delay(100)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            self.update()
            self.draw()

    def update(self):
        for enemy in self.enemies:
            enemy.update()
        self.Joueur.update()

    def draw(self):
        self.app.fill(0)
        for enemy in self.enemies:
            enemy.draw()

        self.food.draw()
        self.Joueur.draw()
        pygame.display.update()
    def checkFoodIntersection(self):
        if math.hypot((self.food.x - self.joueur.xo),(self.food.y - self.joueur.yo)) < FOOD_SIZE + PLAYER_SIZE:
            return True
        else :
            return False
    def checkEnemyIntersection(self,enemy):

        if math.hypot((enemy.pos[0]-self.joueur.xo),(enemy.pos[1]-self.joueur.yo)) < FOOD_SIZE+PLAYER_SIZE :
            return True
        else:
            return False





class Enemy:
    def __init__(self):
        self.app = None
        self.side = 0
        self.pos = (0, 0)
        self.move = (0, 0)

    def update(self):
        x, y = self.pos




        x += self.move[0]
        y += self.move[1]
        if x >= WIDTH - ENEMY_SIZE:
            self.move = (self.move[0] * -1, self.move[1])
        elif x <= 0:
            self.move = (self.move[0] * -1, self.move[1])
        if y >= HEIGHT - ENEMY_SIZE:
            self.move = (self.move[0], self.move[1] * -1)
        elif y <= 0:
            self.move = (self.move[0], self.move[1] * -1)

        self.pos = (x,y)


    def draw(self):
        pygame.draw.circle(self.app, (255, 255, 255), self.pos, ENEMY_SIZE)


class EnemyGenerator:
    def __init__(self):
        self.side = 0

    def generate(self, app):
        enemy = Enemy()
        enemy.side = self.side
        enemy.app = app

        if self.side == 0:
            # top

            xo = random.randint(ENEMY_SIZE, WIDTH - ENEMY_SIZE)
            yo = ENEMY_SIZE

            enemy.pos = (xo, yo)
            enemy.move = (0, ENEMY_MOVE)
        elif self.side == 1:
            # right
            xo = WIDTH - ENEMY_SIZE
            yo = random.randint(ENEMY_SIZE, HEIGHT - ENEMY_SIZE)

            enemy.pos = (xo, yo)
            enemy.move = (-ENEMY_MOVE, 0)
        elif self.side == 2:
            # bottom
            yo = HEIGHT - ENEMY_SIZE
            xo = random.randint(ENEMY_SIZE, WIDTH - ENEMY_SIZE)

            enemy.pos = (xo, yo)
            enemy.move = (0, -ENEMY_MOVE)
        else:
            # left
            xo = ENEMY_SIZE
            yo = random.randint(ENEMY_SIZE, HEIGHT - ENEMY_SIZE)

            enemy.pos = (xo, yo)
            enemy.move = (ENEMY_MOVE, 0)
        self.side = (self.side + 1) % 4
        return enemy
class Joueur:
    def __init__(self,app):
        self.xo= int(WIDTH/2+10)
        self.yo =int(HEIGHT/2)
        self.app = app
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.xo > PLAYER_SIZE:
            self.xo -= PLAYER_MOVE
        if keys[pygame.K_RIGHT] and self.xo < WIDTH - PLAYER_SIZE:
            self.xo += PLAYER_MOVE
        if keys[pygame.K_UP] and self.yo > PLAYER_SIZE:
            self.yo -= PLAYER_MOVE
        if keys[pygame.K_DOWN] and self.yo < HEIGHT - PLAYER_SIZE:
            self.yo += PLAYER_MOVE


    def draw(self):
        pygame.draw.circle(self.app,ORANGE,(self.xo,self.yo),PLAYER_SIZE)
class Food :
    def __init__(self,app):
        self.app = app
        self.x = random.randint(FOOD_SIZE,WIDTH-FOOD_SIZE)
        self.y = random.randint(FOOD_SIZE,HEIGHT-FOOD_SIZE)
    def draw(self):

        pygame.draw.circle(self.app,PINK,(self.x,self.y), FOOD_SIZE)

a= Jeu()


