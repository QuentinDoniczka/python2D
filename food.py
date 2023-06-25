import random
import pygame


class Food:
    def __init__(self, x, y, radius=10):
        self.x = x
        self.y = y
        self.radius = radius
        self.value = radius/5
        # Générer une couleur aléatoire
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def draw(self, display):
        pygame.draw.circle(display, self.color, (self.x, self.y), self.radius)

    # afficher les coordonnée
    def __str__(self):
        return f"Food at ({self.x}, {self.y})"

    def get_position(self):
        return self.x, self.y
