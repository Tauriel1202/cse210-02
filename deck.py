""" 
    Author: Nelson, Courtney M, Benjamin Antonio Huerta Torres 
     Deck
    ...
    This class defines the deck for the game.
    ...

    Attributes
    ----------
    current_card: int
        the value of a card between 1 to 13

    last_card: int
        the last value of a card between 1 to 13
    
    Methods
    -------
    shuffle(self)
        just shuffle the values
    
    next_card(self)
        calculate the next value
"""

import random


class Deck:

    current_card = None
    last_card = random.randint(1,13)
    

    def __init__(self):
        None


    def shuffle(self):
        """ This method change the value to the last card """
        self.last_card = self.current_card

    def next_card(self):
        """ This method calculate the next value """
        self.current_card = random.randint(1,13) #4
        return self.current_card
