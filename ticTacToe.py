"""
This class: 'TicTacToe' may be the most important and central class out of all of them. This class is important
for creating the initial objects that will be used in the game. It also calls for the language selection right in the
front. Along with creating the functions to obtain the move from the 'player' and the 'AI', it contains the essential
'run' function, in which the game will run out of (refer to 'Main'); inside of this also contains the code
to write the results of the game to the file (in either language!).
"""

# These libraries will be used to randomize the AI's moves
# and obtain the date and time for when the match concluded (respectively)
import datetime
import random

# Grabs the data from the 'board.py' and the 'translations.py' file
from board import Board
from translations import Translations


class TicTacToe:

    # Creates a fresh new board and initializes the object and variables
    def __init__(self):
        self.board = Board()  # Create the board as an 'object'
        self.player = 'X'  # Player will take 'X'
        self.ai = 'O'  # AI will take 'O'
        self.translations = None  # By default, no translation will be selected

    # Select your language
    def selectLanguage(self):
        while True:
            choice = input('Choose your language (en/sr): ')
            self.translations = Translations.getTranslations(choice.lower())  # 'lower()' for lowercase letters only

            # Once the language has been selected, exit this loop; otherwise: prompt the user again (due to error)
            if self.translations:
                break
            else:
                print('Invalid language choice. Please try again.')

    # Prompts the user to input a move as an index
    @staticmethod  # No arguments taken; 'self' not needed here
    def getHumanMove():
        while True:
            move = input('Enter your move (0-8): ')

            if move.isdigit() and int(move) in range(9):
                return int(move)
            else:
                print('Invalid move. Please try again.')

    # Creates a list of valid moves and has the AI randomly select a move. Hence: 'import random'
    def getAIMove(self):
        # Iterate through the board to ensure the move is 'valid'
        validMoves = [i for i in range(9) if self.board.isValidMove(i)]

        return random.choice(validMoves)

    # Runs the game in a 'while' loop until the game concludes.
    # Uses 'self.translations()' for implementing multi-lang support
    def run(self):
        self.selectLanguage()
        print(self.translations['welcome'])
        print(self.translations['assignment'])

        self.board.display()

        # While the board is NOT full, keep the game running in a loop
        while not self.board.isBoardFull():
            # Player's turn
            move = self.getHumanMove()
            while not self.board.makeMove(move, 'X'):
                validMoves = [i for i in range(9) if self.board.isValidMove(i)]

                print(self.translations['validMoves'] + str(validMoves))
                move = self.getHumanMove()

            self.board.display()
            if self.board.isWinner('X'):
                print('X' + self.translations['playerWon'])

                break

            # If the board is full after the player's turn, it's a tie
            if self.board.isBoardFull():
                print(self.translations['tie'])

                break

            # AI's turn
            move = self.getAIMove()
            self.board.makeMove(move, 'O')

            print(self.translations['aiPlayed'] + str(move))

            self.board.display()
            if self.board.isWinner('O'):
                print(self.translations['aiWon'])

                break

        # Create and write the results of the game to a file (including board state, date and time, etc.)
        with open("results.txt", "a") as f:
            if self.board.isWinner(self.player):
                f.write(self.translations['winner'] + self.player + "\n")

            elif self.board.isWinner(self.ai):
                f.write(self.translations['aiWon'])

            else:
                f.write("Winner: Tie\n")

            f.write(self.translations['boardState'] + "\n")
            f.write("-----------------\n")

            for i in range(9):
                f.write(f"| {self.board.board[i]} ")

                if (i + 1) % 3 == 0:
                    f.write("|\n")

            f.write("-----------------\n\n")
            f.write(self.translations['dateTime'] + str(datetime.datetime.now()) + "\n\n")
