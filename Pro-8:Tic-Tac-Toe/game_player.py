import math
import random

from numpy import square

class Player:

    def __init__(self, letter):
        self.letter = letter  # Letter is x or o

    def get_moves(self, game):
        pass

class RandomComputerPlayer(Player):

    def __init__(self, letter):
        super().__init__(letter)

    def get_moves(self, game):
        #GET a RANDOM VALID SPOT FOR OUR NEXT MOVE
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(Player):

    def __init__(self, letter):
        super().__init__(letter)

    def get_moves(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + "'s turn. Input moves (0-8): ")
            # We are going to check that is correct value by trying to cast
            # it is an integer, if it's not, then we say its invalid
            # if that spot is not available on the board, we also say it's invalid.
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True 
            except ValueError:
                print("\nInvalid Square. Try again!")
        return val