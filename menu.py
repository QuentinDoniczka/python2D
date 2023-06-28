import pygame
from button import Button


class Menu:
    def __init__(self,game, btn_play, btn_multiplayer, btn_options):
        self.game = game
        self.btn_play = btn_play
        self.btn_multiplayer = btn_multiplayer
        self.btn_options = btn_options

    def handle_events(self):
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # Play button
            if self.btn_play.is_over(pos):
                self.btn_play.color = self.btn_play.highlighted_color
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.game.run()
            else:
                self.btn_play.color = (73,73,73)

            # Multiplayer button
            if self.btn_multiplayer.is_over(pos):
                self.btn_multiplayer.color = self.btn_multiplayer.highlighted_color
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.game.run()  # Implement your multiplayer mode here
            else:
                self.btn_multiplayer.color = (73,73,73)

            # Options button
            if self.btn_options.is_over(pos):
                self.btn_options.color = self.btn_options.highlighted_color
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.game.run()  # Implement your options mode here
            else:
                self.btn_options.color = (73,73,73)

    def draw(self):
        self.btn_play.draw(self.game.display, (0,0,0))
        self.btn_multiplayer.draw(self.game.display, (0,0,0))
        self.btn_options.draw(self.game.display, (0,0,0))

    def run(self):
        while True:
            self.draw()
            self.handle_events()
            pygame.display.update()
