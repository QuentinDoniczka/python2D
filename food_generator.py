import random
from food import Food


class FoodGenerator:
    def __init__(self, x, y, max_food=10000, spawn_rate=10):
        self.x = x
        self.y = y
        self.spawn_rate = spawn_rate
        self.max_food = max_food
        self.food_list = []
        self.time_since_last_spawn = 0

    def generate_food(self):
        x = random.randint(0, self.x)
        y = random.randint(0, self.y)
        self.food_list.append(Food(x, y))

    def draw(self, display):
        for food in self.food_list:
            food.draw(display)

    def update(self, dt):
        self.time_since_last_spawn += dt
        if self.should_generate_food():
            self.generate_food()
            self.time_since_last_spawn = 0

    def get_food_list(self):
        return self.food_list

    def should_generate_food(self):
        return len(self.food_list) < self.max_food and self.time_since_last_spawn >= 1 / self.spawn_rate
