"""
This class is designed to handle the 'multi-lang' function for the program. This class contains two dictionaries:
one for English, and one for Serbian. These data structures will hold the translated text for their various messages
in the game. 'getTranslations' is then used to pull the translations from this file, as the player will have to select the
language of choice at the beginning of the game. The function is a static method, as languageCode is an
entirely new variable that is being created, we are NOT passing through a variable, by any means.

As a result of this new concept, changes have been made to the 'ticTacToe.py' file.
"""


class Translations:
    english = {'welcome': 'Welcome to Tic-Tac-Toe!',
               'languageChoice': 'Choose your language (en/sr): ',
               'aiPlayed': 'The AI played ',
               'playerWon': ' has won!',
               'aiWon': 'The AI has won!',
               'assignment': 'Player is X, AI is O',
               'tie': "It's a tie!",
               'enterMove': 'Enter your move (0-8): ',
               'invalidMove': 'Invalid move. Please try again.',
               'validMoves': 'Invalid move. Valid moves are: ',
               'winner': 'Winner: ',
               'boardState': 'Board State:',
               'dateTime': 'Date and Time: '}

    serbian = {'welcome': 'Добродошли у игру Тик Так Тое!',
               'languageChoice': 'Изаберите језик (ен/ср): ',
               'aiPlayed': 'АИ је одиграо ',
               'playerWon': ' је победио!',
               'aiWon': 'АИ је победио!',
               'assignment': 'Играч је X, АИ је O',
               'tie': 'Нерешено је!',
               'enterMove': 'Унесите свој потез (0-8): ',
               'invalidMove': 'Погрешан потез. Покушајте поново.',
               'validMoves': 'Погрешан потез. Важећи потези су: ',
               'winner': 'Победник: ',
               'boardState': 'Статус табле:',
               'dateTime': 'Датум и време: '}

    @staticmethod  # We are creating a variable here, NOT passing one through
    def getTranslations(languageCode):
        if languageCode == 'en':
            return Translations.english

        elif languageCode == 'sr':
            return Translations.serbian

        else:
            return None
