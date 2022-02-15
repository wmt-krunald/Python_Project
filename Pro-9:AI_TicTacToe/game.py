from game_player import GeniusComputerPlayer, HumanPlayer   

class TicTacToe:

    def __init__(self):
        self.board = [' ' for _ in range(9)] # WE WILL USE SINGLE LIST TO REP 3x3 BOARD.
        self.current_winner = None # Keep Track of winner.
    def print_board(self):

        # Getting row
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod

    def print_board_num():
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')
    
    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' '] #This is contain Abovre whole thing
        # moves = []
        # for (i, x) in enumerate(self.board):
            # #['x','x','0'] --> [(0, x), (1, x), (2, 0)]
            # if spot == " ":
            #     moves,append(i)
            # return moves

    def empty_square(self):
        return " " in self.board

    def make_move(self, square, letter):
        # If valid move then make Move ( assign square to a letter )
        #then return True. If invalid, then return False.
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # Winner if 3 in a row anywhere.. We have to check all of these!
        
        # First Let's check the row
        row_ind = square // 3
        row = self.board[row_ind*3 : (row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True

        # Let's check for Col
        col_ind = square % 3
        col = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in col]):
            return True

        # Let's check for Diagonal
        # But only if the square is an even number (0, 2, 4, 6, 8)
        # These are the only moves possible to win a diagonal.
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]] # This is left to right diagonal
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]] # This is Right to Left diagonal
            if all([spot == letter for spot in diagonal2]):
                return True

        # If all these checks fail then
        return False

    def num_empty_square(self):
        return self.board.count(" ")

def play(game, x_player, o_player, print_game=True):
    # This will return the winner of the game(the letter). or none for tie.
    if print_game:
        game.print_board_num()
    
    letter = "X" # Starting Letter
    # Iterate while the game still has empty square
    # We don't have worry about winner b'cuz we will just return that ..
    # .. which breaks the loop.
    while game.empty_square():
        #get the move from appropreate Player
        if letter == "0":
            square = o_player.get_moves(game)
        else:
            square = x_player.get_moves(game)
        
        # Find Function to make Move
        if game.make_move(square, letter):
            if print_game:
                print(letter + f" makes a move to square {square}")
                game.print_board()
                print("") # Just print empty Line

            if game.current_winner:
                if print_game:
                    print(letter+ " Win !!!!!!!!!!!!!!!!")
                return letter

            # After we make a move, we need to alternate letters

            letter = "0" if letter == "X" else "X" # Above 4 line we did in 1 line
            # if letter == "X":
            #     letter = "0"
            # else:
            #     letter = "X"

        if print_game:
            print("\nIt's Tie.")
        

if __name__ == "__main__":
    x_player = HumanPlayer("X")
    o_player =  GeniusComputerPlayer("0")
    t = TicTacToe()

    play(t, x_player, o_player, print_game=True)