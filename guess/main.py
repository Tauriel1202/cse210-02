from Jumper import Jumper


class Game:
    def start(self):
        jumper = Jumper()
        jumper.play()


def main():
    game = Game()
    game.start()


if __name__ == "__main__":
    main()
