# Tic Tac Toe Ai

This is an AI meant to play tic tac toe, and play it well. Currently, it's a work in progress. Eventually I mean to implement an API where you can feed it a matrix representing the current state of play in a tic tac toe game. It will then recommend the next move. I may then use that to build a tic tac toe gui.

# How it works

Main Principles
-----

The basic idea behind the AI is that it will look at a given board and then consider all possible plays available. For each possible play, it will then consider all the possible plays that could apply there, and so on recursively. The recursion will end either at a specified depth (I.E: Have the AI check up to 5 moves in advance), when a player wins, or when the board fills up and no player can play any longer.

For whatever depth given, it will recommend the move that appears to lead to the most potential wins.

Improvements Over Normal Tic Tac Toe
-----

(In Progress)

This AI is built to work with "tic tac toe boards" of any dimension, provided they are square.

Additonally, the number of X's or O's in a row required to win may also be specified

This means that we could play 4-in-a-row tic tac toe on a 5x5 game board if we'd like to:

 X |   |   |   |
---+---+---+---+---
 O | X |   |   |
---+---+---+---+---
 O |   | X |   |
---+---+---+---+---
 O |   |   | X |
---+---+---+---+---
   |   |   |   |

   X Wins!
