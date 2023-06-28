from my_game import MyGame
from button import Button
from menu import Menu


def main():
    game = MyGame(1920, 1080)

    btn_play = Button(50, 50, 300, 100, 'Play')
    btn_multiplayer = Button(50, 200, 300, 100, 'Multiplayer')
    btn_options = Button(50, 350, 300, 100, 'Options')

    menu = Menu(game, btn_play, btn_multiplayer, btn_options)
    menu.run()


if __name__ == "__main__":
    main()
