import pygame

import food_generator
from player import Player
from food_generator import FoodGenerator  # Assurez-vous d'avoir ce fichier dans le même dossier


pygame.init()

class MyGame:
    def __init__(self, width, height):
        self.size = (width, height)
        self.display = pygame.display.set_mode(self.size)
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.running = True
        self.player = Player(width // 2, height // 2, 50)  # Position initiale au milieu de l'écran, rayon de 15
        self.food_generator = FoodGenerator(width, height)  # Ajout de FoodGenerator
        self.test = 0

    def update(self, dt):
        self.player.update(dt)
        self.test += self.clock.get_time() / 1000
        self.food_generator.update(dt)


    def render(self):
        self.display.fill((173, 216, 230))
        self.food_generator.draw(self.display)
        self.player.draw(self.display)

    def run(self):
        while self.running:
            dt = self.clock.tick(self.fps) / 1000  # Obtenir le temps delta en secondes et crée une pause artificiel
            self.update(dt)
            self.render()
            pygame.display.flip()  # Mettre à jour l'écran complet
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

        pygame.quit()