#This is a game played against the computer in the command line.
#I modified a game with computer play because I needed the logic.
#Thanks to Sean Halverson on YouTube for the base logic to play
#against the computer.

import random

print("Welcome to Tic Tac Toe")
print("----------------------")

possibleNumbers = [1,2,3,4,5,6,7,8,9]
gameBoard = [[1,2,3], [4,5,6], [7,8,9]]
rows = 3
cols = 3

def printGameBoard():
  for x in range(rows):
    print("\n+---+---+---+")
    print("|", end="")
    for y in range(cols):
      print("", gameBoard[x][y], end=" |")
  print("\n+---+---+---+")

#Modifying the array per turn
def modifyArray(num, turn): 
    row, col = divmod(num - 1, 3)
    gameBoard[row][col] = turn

#Check for a winner
def checkForWinner(gameBoard):
    # Check rows and columns
    for i in range(3):
        if gameBoard[i][0] == gameBoard[i][1] == gameBoard[i][2] and gameBoard[i][0] != ' ':
            print(f"{gameBoard[i][0]} has won!")
            return gameBoard[i][0]
        if gameBoard[0][i] == gameBoard[1][i] == gameBoard[2][i] and gameBoard[0][i] != ' ':
            print(f"{gameBoard[0][i]} has won!")
            return gameBoard[0][i]

    # Check diagonals
    if gameBoard[0][0] == gameBoard[1][1] == gameBoard[2][2] and gameBoard[0][0] != ' ':
        print(f"{gameBoard[0][0]} has won!")
        return gameBoard[0][0]
    if gameBoard[0][2] == gameBoard[1][1] == gameBoard[2][0] and gameBoard[0][2] != ' ':
        print(f"{gameBoard[0][2]} has won!")
        return gameBoard[0][2]
    else:
        return "N"


leaveLoop = False
turnCounter = 0

while(leaveLoop == False):
  ### It's the player turn
  if(turnCounter % 2 == 0):
    printGameBoard()
    numberPicked = int(input("\nChoose a number [1-9]: "))
    if(numberPicked >= 1 or numberPicked <= 9):
      modifyArray(numberPicked, 'X')
      possibleNumbers.remove(numberPicked)
    else:
      print("Invalid input. Please try again.")
    turnCounter += 1
  ### It's the computer's turn
  else:
    while(True):
      computer = random.choice(possibleNumbers)
      print("\nComputer: ", computer)
      if(computer in possibleNumbers):
        modifyArray(computer, 'O')
        possibleNumbers.remove(computer)
        turnCounter += 1
        break
  
  winner = checkForWinner(gameBoard)
  if(winner != "N"):
    print("\nGame over! Thank you for playing :)")
    break