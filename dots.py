import pygame
import random
import math
from tkinter import *
from tkinter import messagebox

# INITIALISATION DES VARIABLES GLOBALES

LONGUEUR = 700
HAUTEUR = 400
TAILLE_NOURRITURE = 5
TAILLE_ENNEMI = 11
TAILLE_JOUEUR = 20
DÉPLACEMENT_ENNEMI = 10
ROUGE = (220, 20, 60)
ORANGE = (238, 118, 0)
DÉPLACEMENT_JOUEUR = 20
ROSE = (255, 105, 180)

# FIN DE L'INITIALISATION

class Jeu:

    def __init__(self):
        self.score = 0
        # Création de la fenêtre du jeu
        self.app = pygame.display.set_mode((LONGUEUR, HAUTEUR), )
        pygame.display.set_caption('Dots')
        self.joueur = Joueur(self.app)
        self.générateur = GenerateurEnnemi()
        self.ennemis = []
        self.nourriture = Nourriture(self.app)

        ennemi = self.générateur.générer(self.app)
        self.ennemis.append(ennemi)
        self.lancer = True
        # Boucle pour mêttre à jour l'application et dessiner les objets
        while self.lancer:
            pygame.time.delay(100)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.lancer = False
            self.miseÀJour()
            self.dessiner()

    def miseÀJour(self):
        ''' Mets à jour les positions des ennemis, du joueur et de la nourriture et vérifie les intersections. '''
        for ennemi in self.ennemis:
            ennemi.miseÀJour()
            if self.vérifierIntersectionEnnemi(ennemi):
                Tk().wm_withdraw()
                messagebox.showinfo('Jeu Perdu', 'Score: ' + str(self.score))
                self.lancer = False
        self.joueur.miseÀJour()
        if self.vérifierIntersectionNourriture():
            ennemi = self.générateur.générer(self.app)
            self.ennemis.append(ennemi)
            self.nourriture = Nourriture(self.app)
            self.score += 1

    def dessiner(self):
        ''' Dessine les ennemies, le joueur et la nourriture à leurs nouvelles positions.'''
        self.app.fill(0)
        for ennemi in self.ennemis:
            ennemi.dessiner()

        self.nourriture.dessiner()
        self.joueur.dessiner()
        pygame.display.update()

    def vérifierIntersectionNourriture(self):
        ''' Vérifie si la distance entre le centre du joueur et de la nourriture est plus petite que la somme des rayons de ces deux objets.'''
        if math.hypot((self.nourriture.x - self.joueur.xo),
                      (self.nourriture.y - self.joueur.yo)) < TAILLE_NOURRITURE + TAILLE_JOUEUR:
            return True
        else:
            return False

    def vérifierIntersectionEnnemi(self, ennemi):
        ''' Vérifie si la distance entre le centre du joueur et des ennemis est plus petite que la somme des rayons de ces deux objets.'''
        if math.hypot((ennemi.pos[0] - self.joueur.xo),
                      (ennemi.pos[1] - self.joueur.yo)) < TAILLE_NOURRITURE + TAILLE_JOUEUR:
            return True
        else:
            return False


class Ennemi:
    def __init__(self):
        self.app = None
        self.côté = 0
        self.pos = (0, 0)
        self.déplacement = (0, 0)

    def miseÀJour(self):
        ''' Mets à jour la position d'un ennemi et délimite le déplacement de l'ennemi. '''
        x, y = self.pos

        x += self.déplacement[0]
        y += self.déplacement[1]
        if x >= LONGUEUR - TAILLE_ENNEMI:
            self.déplacement = (self.déplacement[0] * -1, self.déplacement[1])
        elif x <= TAILLE_ENNEMI:
            self.déplacement = (self.déplacement[0] * -1, self.déplacement[1])
        if y >= HAUTEUR - TAILLE_ENNEMI:
            self.déplacement = (self.déplacement[0], self.déplacement[1] * -1)
        elif y <= TAILLE_ENNEMI:
            self.déplacement = (self.déplacement[0], self.déplacement[1] * -1)

        self.pos = (x, y)

    def dessiner(self):
        ''' Dessine un ennemi.'''
        pygame.draw.circle(self.app, (255, 255, 255), self.pos, TAILLE_ENNEMI)


class GenerateurEnnemi:
    def __init__(self):
        self.côté = 0

    def générer(self, app):
        ''' Crée un ennemi dans un des 4 côtés de l'écran'''
        ennemi = Ennemi()
        ennemi.côté = self.côté
        ennemi.app = app

        if self.côté == 0:
            # Haut de l'écran
            xo = random.randint(TAILLE_ENNEMI, LONGUEUR - TAILLE_ENNEMI)
            yo = TAILLE_ENNEMI

            ennemi.pos = (xo, yo)
            ennemi.déplacement = (0, DÉPLACEMENT_ENNEMI)
        elif self.côté == 1:
            # Côté droit de l'écran
            xo = LONGUEUR - TAILLE_ENNEMI
            yo = random.randint(TAILLE_ENNEMI, HAUTEUR - TAILLE_ENNEMI)

            ennemi.pos = (xo, yo)
            ennemi.déplacement = (-DÉPLACEMENT_ENNEMI, 0)
        elif self.côté == 2:
            # Bas de l'écran
            yo = HAUTEUR - TAILLE_ENNEMI
            xo = random.randint(TAILLE_ENNEMI, LONGUEUR - TAILLE_ENNEMI)

            ennemi.pos = (xo, yo)
            ennemi.déplacement = (0, -DÉPLACEMENT_ENNEMI)
        else:
            # Côté gauche de l'écran
            xo = TAILLE_ENNEMI
            yo = random.randint(TAILLE_ENNEMI, HAUTEUR - TAILLE_ENNEMI)

            ennemi.pos = (xo, yo)
            ennemi.déplacement = (DÉPLACEMENT_ENNEMI, 0)
        self.côté = (self.côté + 1) % 4
        return ennemi


class Joueur:
    def __init__(self, app):
        self.xo = int(LONGUEUR / 2 + 10)
        self.yo = int(HAUTEUR / 2)
        self.app = app

    def miseÀJour(self):
        '''Mets à jour la position du joueur'''
        clés = pygame.key.get_pressed()
        if clés[pygame.K_LEFT] and self.xo > TAILLE_JOUEUR:
            self.xo -= DÉPLACEMENT_JOUEUR
        if clés[pygame.K_RIGHT] and self.xo < LONGUEUR - TAILLE_JOUEUR:
            self.xo += DÉPLACEMENT_JOUEUR
        if clés[pygame.K_UP] and self.yo > TAILLE_JOUEUR:
            self.yo -= DÉPLACEMENT_JOUEUR
        if clés[pygame.K_DOWN] and self.yo < HAUTEUR - TAILLE_JOUEUR:
            self.yo += DÉPLACEMENT_JOUEUR

    def dessiner(self):
        ''' Dessine le joueuer'''
        pygame.draw.circle(self.app, ORANGE, (self.xo, self.yo), TAILLE_JOUEUR)


class Nourriture:
    def __init__(self, app):
        self.app = app
        self.x = random.randint(TAILLE_NOURRITURE, LONGUEUR - TAILLE_NOURRITURE)
        self.y = random.randint(TAILLE_NOURRITURE, HAUTEUR - TAILLE_NOURRITURE)

    def dessiner(self):
        '''Dessine la nourriture'''
        pygame.draw.circle(self.app, ROSE, (self.x, self.y), TAILLE_NOURRITURE)


a = Jeu()
