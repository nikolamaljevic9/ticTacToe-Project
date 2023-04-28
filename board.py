"""
This class defines the 'Board' object. This object will allow for the development of
the '3x3' Tic Tac Toe board game and the logic associated with it, including generating the proper layout of the board
with | (refer to 'display' function), checking if the winning conditions have been met (including diagonally), etc.
"""


class Board:
    # Class constructor
    def __init__(self):
        self.board = [' ' for _ in range(9)]

    # Create the 3x3 'grid'
    def display(self):
        print(f"| {self.board[0]} | {self.board[1]} | {self.board[2]} |")
        print(f"| {self.board[3]} | {self.board[4]} | {self.board[5]} |")
        print(f"| {self.board[6]} | {self.board[7]} | {self.board[8]} |")

    # Is this move valid?
    def isValidMove(self, move):
        return self.board[move] == ' '

    # Deploy the symbol onto the designated position
    def makeMove(self, move, symbol):
        if self.isValidMove(move):
            self.board[move] = symbol

            return True

        return False

    def isWinner(self, symbol):
        # Check for horizontal wins
        for i in range(0, 9, 3):
            if self.board[i:i + 3] == [symbol] * 3:
                return True

        # Check for vertical wins
        for i in range(3):
            if self.board[i::3] == [symbol] * 3:
                return True

        # Check for diagonal wins
        if self.board[0] == symbol and self.board[4] == symbol and self.board[8] == symbol:
            return True

        elif self.board[2] == symbol and self.board[4] == symbol and self.board[6] == symbol:
            return True

        else:
            return False

    # Is the board full?
    def isBoardFull(self):
        return ' ' not in self.board
