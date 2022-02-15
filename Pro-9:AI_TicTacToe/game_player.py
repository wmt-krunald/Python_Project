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
    
class GeniusComputerPlayer(Player):

    def __init__(self, letter):
        super().__init__(letter)

    def  get_moves(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())  # Random choose 
        else:
            # Otherwise, Now we get the square based on Minimax algorithm
            square = self.minimax(game, self.letter)["position"]
        return square
    
    def minimax(self, ss, player):
        max_player = self.letter  # Yourself!!!!!!!!
        other_player = "0" if player == "X" else "X"

        # First we check if previous move is winner or not!!!!
        # This is our base case
        if ss.current_winner == other_player:
            # We should return position and score. b'cuz we need to keep track of score
            # For Minimax to work

            return {"position": None,
                    "score": 1 * (ss.num_empty_square() + 1) if other_player == max_player else -1 * (
                            ss.num_empty_square() + 1)
                    }
        elif ss.empty_square():  # No empty square
            return {"position": None,  "score": 0}
        
        if player == max_player:
            best = {"position": None, "score": -math.inf} # Each score should be maximize(be larger)
        else:
            best = {"position": None, "score": math.inf} #Each score should be minimize

        for possible_moves in ss.available_moves():
            # STEP 1: Make a move, try to spot 
            ss.make_move(possible_moves, player)

            # STEP 2: Recurse using minimax, to simulate a game after making that move            
            simu_score = self.minimax(ss, other_player) # Now we alternates player  

            # STEP 3: Undo the Move
            ss.board[possible_moves] = " "
            ss.current_winner = None
            simu_score["position"] = possible_moves # Otherwise this will get messed up from recursion

            # STEP 4: Update the dictionaries if necessary
            if player == max_player: # We are trying to maximize the max_player
                if simu_score["score"] > best["score"]:
                    best = simu_score # Replace best
            else:
                if simu_score["score"] < best["score"]:
                    best = simu_score # Replace best
        return best