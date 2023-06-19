import pygame
import math

class Player:
    def __init__(self, x, y, radius, color=(255, 0, 0)):  # x et y sont la position initiale du joueur, radius est le rayon du cercle
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.accumulator = 0
        self.speed = 1000

    def draw(self, display):
        pygame.draw.circle(display, self.color, (self.x, self.y), self.radius)

    def update(self, dt):
        self.accumulator += dt
        if self.accumulator >= 0.05:  # Si plus d'une seconde s'est écoulée
            self.accumulator -= 0.05  # Soustraire une seconde de l'accumulateur
            if self.radius > 100:
                self.radius = 50
            else:
                self.grow()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_z]:  # Déplacer vers le haut avec la touche "z"
            self.y -= self.speed * dt
        if keys[pygame.K_s]:  # Déplacer vers le bas avec la touche "s"
            self.y += self.speed * dt
        if keys[pygame.K_q]:  # Déplacer vers la gauche avec la touche "q"
            self.x -= self.speed * dt
        if keys[pygame.K_d]:  # Déplacer vers la droite avec la touche "d"
            self.x += self.speed * dt

        mouse_x, mouse_y = pygame.mouse.get_pos()  # Récupérer la position de la souris
        dx, dy = mouse_x - self.x, mouse_y - self.y  # Calculer le déplacement nécessaire pour atteindre la souris
        dist = math.hypot(dx, dy)  # Calculer la distance à la souris

        if dist:  # Eviter une division par zéro si la souris est déjà sur le joueur
            dx /= dist  # Normaliser le déplacement pour obtenir un vecteur unitaire
            dy /= dist  # Normaliser le déplacement pour obtenir un vecteur unitaire
            self.x += dx * self.speed * dt  # Appliquer le déplacement
            self.y += dy * self.speed * dt  # Appliquer le déplacement

    def grow(self):
        self.radius += 1
