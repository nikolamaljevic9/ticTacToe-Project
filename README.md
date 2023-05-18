Name: Nikola Maljevic
Version: 2.0
Class: Computer Science 132: Intermediate Programming
Assignment: Project Deliverable 3 (Final Version of the Tic Tac Toe Game with AI)

Purpose: After delving more into Object-Oriented Programming concepts, I decided I wanted to try something unique
with this project that I have not attempted since High School with the Java Programming Language in the
'AP Computer Science A' curriculum. I have decided that I wanted to attempt to modulate this project and
split each and every class into files. It helps to keep things more organized and prevent a 'runoff'. Each file is
representative of the class, and the next one imports all the data from the previous one. I have also redesigned the
code, so that upon completion of the game, the program will write to 'results.txt', the winner of the game, and the
board's state. While developing this project, a thought had occurred. During a lecture in class, I remember our
instructor utilizing the 'datetime' library of Python. I thought: "Wouldn't it be cool if not only I printed the winner
and board state, but the date and time as well!" I have incorporated this concept within the 'ticTacToe' class itself
within the 'class run(self)' function.

I have mentioned this idea to my family, and some of them do not speak or
understand English very well, so I have now implemented 'multi-lang' support for this game as well via dictionaries.
The user now has the ability to select between 'English' and 'Serbian' at the start of the game. As a result of this
new class, changes have been made to the 'ticTacToe.py' file.

The 'Artificial Intelligence' that is used within this program essentially relies on the 'random' library, and its
methods to randomize the AI's output. Theoretically, you could the min and max functions within Python to make the
computer 'exceptionally challenging' to play against, but I decided not to do that, because this is supposed to be fun,
not stressing.

As per request, I have also created a testCase file for the program, so that we may test some of the program's
functions to verify that everything works as expected. To run this unitTest, make sure to set the configuration of the
program to run from 'test_ticTacToe.py' and not 'main.py'.

NOTE: When playing this game, it is important to note that the 'move' is representative of the array's index.
This means that the move can also be '0', which would be considered the very first position (top left corner)
of the board.

