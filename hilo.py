
from deck import Deck

"""
TODO: Validations and doc
"""  
class hilo(): 


  deck = None
  points = 300
  

  def __init__(self): 
    self.deck = Deck()


  def play(self):

    """ This method has the game logic """
    while self.is_game_over() != True:

      print(f"\nThe card is:{self.deck.last_card}")
      option = input("Higher or Lower? [l/h]")
      print(f"The next card was: {self.deck.next_card()}")

      """ This block of code check if add points or not """
      if (self.deck.current_card > self.deck.last_card ) and (option != 'l'):
         self.points+= 100
      elif (self.deck.current_card < self.deck.last_card ) and (option != 'h'): 
          self.points+=100
      else:
          self.points -=75
      """ end add points or not """

      print(f"Your score is: {self.points}")
      self.deck.shuffle() #updating the values
      play = input(f"Play again? [y/N] ")
      if(play != 'y'):
        break

  def is_game_over(self):
    """This method check the points"""
    if self.points <= 0:
      return True
    else: 
      return False   
