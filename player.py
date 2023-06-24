import pygame


class Player:
    def __init__(self, x, y, radius, color=(255, 0, 0), max_speed=500, growth_rate=1, friction=0.9, speed=1000, update_interval=0.05, max_radius=100, min_radius=50, max_distance=100):
        self.position = pygame.Vector2(x, y)
        self.radius = radius
        self.color = color
        self.max_speed = max_speed
        self.growth_rate = growth_rate
        self.friction = friction
        self.speed = speed
        self.update_interval = update_interval
        self.max_radius = max_radius
        self.min_radius = min_radius
        self.max_distance = max_distance
        self.accumulator = 0
        self.velocity = pygame.Vector2(0, 0)
        self.acceleration = pygame.Vector2(0, 0)

    def draw(self, display):
        pygame.draw.circle(display, self.color, (int(self.position.x), int(self.position.y)), self.radius)

    def update(self, dt):
        # Gestion de la croissance et du mouvement du joueur
        self.accumulator += dt
        if self.accumulator >= self.update_interval:
            self.accumulator -= self.update_interval
            self.manage_growth()

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

    def manage_growth(self):
        # Gérer la croissance du joueur
        if self.radius >= self.max_radius:
            self.radius = self.min_radius
        else:
            self.radius += self.growth_rate
