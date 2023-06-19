import pygame


class Player:
    def __init__(self, x, y, radius, color=(255, 0, 0)):  # x et y sont la position initiale du joueur, radius est le rayon du cercle
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.accumulator = 0

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

    def grow(self):
        self.radius += 1
