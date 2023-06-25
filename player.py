import pygame


class Player:
    def __init__(self, x, y, radius, color=(255, 0, 0)):
        self.position = pygame.Vector2(x, y)
        self.radius = radius
        self.color = color

        self.velocity = pygame.Vector2(0, 0)
        self.acceleration = pygame.Vector2(0, 0)
        self.max_speed = 500
        self.friction = 0.9
        self.speed = 1000

        self.max_radius = 100
        self.min_radius = 30
        self.max_distance = 100

        self.aging_rate = 0.01
        self.smooth_aging_rate = self.aging_rate / 10
        self.aging_interval = 2
        self.smooth_aging_interval = self.aging_interval / 10
        self.time_since_last_aging = 0

        self.font = pygame.font.Font(None, 32)  # None for default system font, 32 for font size

    def draw(self, display):
        pygame.draw.circle(display, self.color, (int(self.position.x), int(self.position.y)), self.radius)

        size_text = self.font.render(str(int(self.radius)), True, (255, 255, 255))  # Create a Surface with the text
        text_rect = size_text.get_rect(center=self.position)  # Get the rectangle enclosing the text
        display.blit(size_text, text_rect)  # Draw the text on the screen at the player's position

    def update(self, dt):
        # Gestion de la croissance et du mouvement du joueur
        self.time_since_last_aging += dt
        if self.time_since_last_aging >= self.smooth_aging_interval:
            self.time_since_last_aging -= self.smooth_aging_interval
            self.age()

        self.update_movement(dt)

    def update_movement(self, dt):
        # Mise à jour de l'accélération, de la vélocité et de la position du joueur
        direction = pygame.mouse.get_pos() - self.position
        distance = direction.length()

        if distance != 0:
            self.update_acceleration(direction.normalize(), distance)

        self.update_velocity(dt, distance)
        self.apply_speed_limit_and_friction()

        self.position += self.velocity * dt

    def update_acceleration(self, direction, dist):
        # Mise à jour de l'accélération du joueur en fonction de la direction de la souris
        self.acceleration = direction

    def update_velocity(self, dt, dist):
        # Mise à jour de la vélocité du joueur en fonction de l'accélération et de la distance à la souris
        acceleration_modifier = min(dist / self.max_distance, 1)
        self.velocity += self.acceleration * self.speed * dt * acceleration_modifier

    def apply_speed_limit_and_friction(self):
        # Application de la friction et de la limite de vitesse au joueur
        speed = self.velocity.length()
        if speed > self.max_speed:
            self.velocity.scale_to_length(self.max_speed)

        self.velocity *= self.friction

    def eat(self, food_value):
        # Increase player radius by food value
        self.radius += food_value
        # Make sure player does not exceed max_radius
        self.radius = min(self.radius, self.max_radius)
        self.update_font()

    def age(self):
        # Decrease player radius by 1% every aging_interval seconds
        self.radius -= self.radius * self.smooth_aging_rate
        # Make sure player does not go below min_radius
        self.radius = max(self.radius, self.min_radius)
        self.update_font()

    def update_font(self):
        # Update the font size according to the radius
        # You can adjust the multiplier to get a font size that looks good for your game
        font_size = int(10 + self.radius * 0.5)  # Change the multiplier to get a different font size
        self.font = pygame.font.Font(None, font_size)