import pygame
pygame.init()

class MyGame:
    def __init__(self, width, height):
        self.size = (width, height)
        self.display = pygame.display.set_mode(self.size)
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.running = True

    def update(self, dt):

        pass

    def render(self):

        pass

    def run(self):
        while self.running:
            dt = self.clock.tick(self.fps) / 1000  # Obtenir le temps delta en secondes
            self.update(dt)
            self.render()
            pygame.display.flip()  # Mettre à jour l'écran complet
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

        pygame.quit()