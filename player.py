import pygame


class Player:
    def __init__(self, x, y, growth, color=(255, 0, 0)):
        self.position = pygame.Vector2(x, y)
        self.growth = growth
        self.color = color
        self.growth_factor = 0.70
        self.radius = 0

        self.velocity = pygame.Vector2(0, 0)
        self.friction = 0.95
        self.acceleration = 800
        self.max_speed = 1000
        self.max_distance = 100

        self.max_growth = 1000000
        self.min_growth = 30

        self.aging_rate = 0.01
        self.smooth_aging_rate = self.aging_rate / 10
        self.aging_interval = 2
        self.smooth_aging_interval = self.aging_interval / 10
        self.time_since_last_aging = 0

        self.font = pygame.font.Font(None, 32)
        self.speed_font = pygame.font.Font(None, 24)

        self.update_radius()

    def draw(self, display):
        pygame.draw.circle(display, self.color, (int(self.position.x), int(self.position.y)), self.radius)

        # size_text
        size_text = self.font.render(str(int(self.growth)), True, (255, 255, 255))
        size_text_rect = size_text.get_rect(center=self.position - pygame.Vector2(0, 10))
        display.blit(size_text, size_text_rect)

        # speed_text
        speed_text = self.speed_font.render(str(int(self.velocity.length())), True, (255, 255, 255))
        speed_text_rect = speed_text.get_rect(center=self.position + pygame.Vector2(0, 10))
        display.blit(speed_text, speed_text_rect)

    def update(self, dt):
        self.time_since_last_aging += dt
        if self.time_since_last_aging >= self.smooth_aging_interval:
            self.time_since_last_aging -= self.smooth_aging_interval
            self.age()
        self.update_movement(dt)

    def update_movement(self, dt):
        direction = pygame.mouse.get_pos() - self.position
        distance = direction.length()

        if distance != 0:
            direction.normalize_ip()
            acceleration_modifier = min(distance / self.max_distance, 1)
            self.velocity += direction * self.acceleration * dt * acceleration_modifier

        if self.velocity.length() > self.max_speed:
            self.velocity.scale_to_length(self.max_speed)

        self.velocity *= self.friction
        self.position += self.velocity * dt

    def update_radius(self):
        self.radius = 30 + (self.growth**self.growth_factor)

    def eat(self, food_value):
        self.growth = min(self.growth + food_value, self.max_growth)
        self.update_radius()
        self.update_font()

    def age(self):
        self.growth = max(self.growth - self.growth * self.smooth_aging_rate, self.min_growth)
        self.update_radius()
        self.update_font()

    def update_font(self):
        font_size = int(10 + self.radius * 0.5)
        self.font = pygame.font.Font(None, font_size)

    def is_point_inside(self, x, y):
        return self.position.distance_to((x, y)) <= self.radius + 1
