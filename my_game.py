import pygame
from player import Player
from food_generator import FoodGenerator

pygame.init()


class MyGame:
    def __init__(self, width, height):
        self.size = (width, height)
        self.display = pygame.display.set_mode(self.size)
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.running = True
        self.player = Player(width // 2, height // 2, 30)
        self.food_generator = FoodGenerator(width, height)
        self.accumulated_time = 0

    def update(self, dt):
        self.player.update(dt)
        self.food_generator.update(dt)
        self.accumulated_time += dt
        if self.accumulated_time >= 0.05:
            self.check_food_collision()
            self.accumulated_time = 0

    def render(self):
        self.display.fill((173, 216, 230))
        self.food_generator.draw(self.display)
        self.player.draw(self.display)

    def run(self):
        while self.running:
            dt = self.clock.tick(self.fps) / 1000
            self.update(dt)
            self.render()
            pygame.display.flip()
            self.handle_events()
        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def check_food_collision(self):
        # Retrieve the list of food instances
        food_list = self.food_generator.get_food_list()

        # List comprehension to filter out the food instances that collide with the player
        # The 'is_point_inside' method is used from the Player class to check the collision
        food_to_remove = [food for food in food_list if self.player.is_point_inside(*food.get_position())]

        # Iterate over each food instance in the food_to_remove list
        # Each food instance is 'eaten' by the player and removed from the original food list
        for food in food_to_remove:
            self.player.eat(2)
            food_list.remove(food)
