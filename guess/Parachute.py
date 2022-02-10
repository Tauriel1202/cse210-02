
class Parachute:
    def __init__(self):
        self.__last_state = 8
        self.__figure_state = [
            " ___\n/___\\\n\\   /\n \\ /\n  o\n /|\\\n / \\",
            " \n/___\\\n\\   /\n \\ /\n  o\n /|\\\n / \\",  # ___
            " \n ___\\\n\\   /\n \\ /\n  o\n /|\\\n / \\",  # //////
            " \n ___\n\\   /\n \\ /\n  o\n /|\\\n / \\",  # //////
            " \n    \n\\   /\n \\ /\n  o\n /|\\\n / \\",  # ___
            " \n    \n    /\n \\ /\n  o\n /|\\\n / \\",  # ///
            " \n    \n    \n \\ /\n  o\n /|\\\n / \\",  # ////
            " \n    \n    \n   /\n  o\n /|\\\n / \\",  # ////
            " \n    \n    \n    \n  x\n /|\\\n / \\"  # ////
        ]

    def print(self, errors):
        if (errors >= self.__last_state):
            print(self.__figure_state[self.__last_state])
        else:
            print(self.__figure_state[errors])
        print("^^^^^^")

    def last_state(self):
        return self.__last_state
