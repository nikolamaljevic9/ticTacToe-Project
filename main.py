"""
The 'Main' class is responsible for holding the main function
that runs the entire game. Since it is not declared in either of the class'
we have it defined here. In this class, the data is imported, and the object is created and the method is called
to run the 'TicTacToe' game.
"""

# Grabs the data from the 'ticTacToe.py' file
from ticTacToe import TicTacToe


class Main:
    if __name__ == '__main__':
        game = TicTacToe()
        game.run()
