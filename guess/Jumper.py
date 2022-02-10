from Parachute import Parachute
from Word import Word


class Jumper:

    def __init__(self):
        self.__word = Word().get_random_word()
        self.__correct = []
        self.__incorrect = []
        self.__figure = Parachute()

    def play(self):
        print(self.__word)

        Word.show_blanks(self.__word, self.__correct)
        self.__figure.print(len(self.__incorrect))

        while (len(self.__incorrect) < figure.last_state()):
            option = input("Guess a letter [a-z]: ")
            if option in self.__word:
                self.__correct.append(option)
            else:
                self.__incorrect.append(option)

            Word.show_blanks(self.__word, self.__correct)
            self.__figure.print(len(self.__incorrect))

    def win(self):

        # self.__figure.last_state() --> lives

        # if (self.__figure.last_state() !=  and win !=True):

        return False
