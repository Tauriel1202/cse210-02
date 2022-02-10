import random


class Word:
    __word_list = ['harass', 'format', 'dressing', 'spread', 'carbon', 'digital', 'haunt', 'challenge', 'sausage', 'systematic', 'sink', 'gene', 'diet', 'strange', 'minimize', 'ambiguous', 'compact', 'conscience', 'angle', 'flex', 'nun', 'settlement', 'camp', 'giant',
                   'cultivate', 'angel', 'equinox', 'board', 'lid', 'view', 'soprano', 'champagne', 'environment', 'econobox', 'twist', 'legislature', 'text', 'agency', 'defend', 'tooth', 'force', 'ethnic', 'wheel', 'repeat', 'essential', 'swipe', 'leader', 'steep', 'cultural', 'counter']

    def _word_list(self, list):
        self.__word_list = list

    def get_random_word(self):
        return random.choice(self.__word_list)

    def show_blanks(word, correct):
        to_print = ""
        for char in word:
            if(char in correct):
                to_print += char
            else:
                to_print += " - "
        print(to_print)
