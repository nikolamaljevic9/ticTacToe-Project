"""
The 'TestTicTacToe' class is responsible for creating unit tests from various functions that exist
throughout the game's program. This class ensures that the functions within the game work properly
and without error. This is important, as even though during some basic test the program seems to work fine,
something may arise in the future that breaks the program, due to perhaps more complicated executions
that the program was not perhaps designed to handle.
"""

import unittest

from board import Board
from ticTacToe import TicTacToe


class TestTicTacToe(unittest.TestCase):

    # Test that the board is initialized with all blank spots, via the 'board' constructor
    def test_boardInitialization(self):
        board = Board()

        self.assertEqual(board.board, [' '] * 9)

    # Test that all moves (valid and/or invalid) can be identified, via 'isValidMove' method
    def test_isValidMove(self):
        board = Board()
        board.board = ['X', ' ', 'O',
                       ' ', ' ', ' ',
                       ' ', ' ', ' ']

        self.assertTrue(board.isValidMove(1))  # You should be able to make a move here
        self.assertFalse(board.isValidMove(0))  # You should NOT be able to make a move here
        self.assertFalse(board.isValidMove(2))  # You should NOT be able to make a move here

    # Test that the player can place their symbol on the board, via 'makeMove' method
    def test_makeMove(self):
        board = Board()
        result = board.makeMove(1, 'X')

        self.assertTrue(result)  # The move was made
        self.assertEqual(board.board[1], 'X')  # Confirmation

    # Test to end the game if the winning conditions were met (by three in a row), via 'isWinner' method
    def test_isWinner(self):
        board = Board()
        board.board = ['X', 'X', 'X',
                       'O', 'O', ' ',
                       ' ', ' ', ' ']

        self.assertTrue(board.isWinner('X'))  # 'X' should win here
        self.assertFalse(board.isWinner('O'))  # 'O' should NOT win here, including a tie

    # Test to determine if the board is full or not (tie), via 'isBoard' method
    def test_isBoardFull(self):
        board = Board()
        board.board = ['X', 'O', 'X',
                       'O', 'O', 'X',
                       'X', 'X', 'O']

        self.assertTrue(board.isBoardFull())  # The board is full

    # Test to check if 'isWinner' returns False when there is no winner
    def test_isWinnerFalse(self):
        board = Board()
        board.board = ['X', 'O', 'X',
                       'O', 'O', 'X',
                       'X', 'X', ' ']

        self.assertFalse(board.isWinner('X'))  # 'X' has NOT won; lost

    # Test to check if 'makeMove' returns False when move is not valid
    def test_makeMoveFalse(self):
        board = Board()
        board.board = ['X', ' ', 'O',
                       ' ', ' ', ' ',
                       ' ', ' ', ' ']

        result = board.makeMove(0, 'X')

        self.assertFalse(result)  # That is an invalid move (regardless of symbol); return 'False'

    # Test to check if 'isBoardFull' returns False when the board is not full
    def test_isBoardFullFalse(self):
        board = Board()
        board.board = ['X', 'O', 'X',
                       'O', 'O', 'X',
                       'X', ' ', ' ']

        self.assertFalse(board.isBoardFull())  # The board is NOT full

    # Tests to ensure there is no default language set via 'selectLanguage'
    def test_selectLanguage(self):
        game = TicTacToe()
        game.selectLanguage()

        self.assertIsNotNone(game.translations)  # There should be no default langauge; user input needed at start


# Main function to execute the unitTest via the object's method (can even be done without it)
if __name__ == '__main__':
    # Run ALL the 9-unit tests
    unittest.main()
