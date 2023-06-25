import pygame

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
        self.players = []  # Define self.players as an empty list
        self.players.append(Player(width // 2, height // 2, 100))  # Add a Player to the list
        self.food_generator = FoodGenerator(width, height)  # Ajout de FoodGenerator

    def update(self, dt):
        for player in self.players:  # Update each player
            player.update(dt)
        self.food_generator.update(dt)

    def render(self):
        self.display.fill((173, 216, 230))
        self.food_generator.draw(self.display)
        for player in self.players:  # Draw each player
            player.draw(self.display)

    def run(self):
        while self.running:
            dt = self.clock.tick(self.fps) / 1000  # Obtenir le temps delta en secondes et crée une pause artificiel
            self.update(dt)
            self.render()
            pygame.display.flip()  # Mettre à jour l'écran complet
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

    def check_food_collision(self):
        foodlist = self.food_generator.get_food_list()
        for self.player in self.players:
            for food in foodlist:
                pass # TODO air de colision entre food et joueur



pygame.quit()
