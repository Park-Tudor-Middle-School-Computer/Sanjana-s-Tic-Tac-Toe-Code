#The websites I used for help on this aret the following:
#https://www.datacamp.com/community/tutorials/functions-python-tutorial
#https://www.programiz.com/python-programming/function
#https://medium.com/byte-tales/the-classic-tic-tac-toe-game-in-python-3-1427c68b8874

#i imported random so I can use it to randomly pick if the computer, or user goes first
import random

#i made a fucntion to draw the board so that the user can see where they are placing their X or O
def drawBoard(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')

#Explaination for the user as to how to place their X and O and what each box is labeled as
print("(The following information is to help you understand the tic tac toe board and where you are moving for your turns.).")
print("The board tic tac toe board is set up from left to right, top to bottom (in numerical order).")
print("The top left corner is called 1. So when you want to place your X or O on that place, and the game asks you to input a place, you would type 1.")
print("The place to the right of that is 2, and the one next to that is 3")
print("In the second row, the first place is 4, the second place is 5, and the third place is 6.")
print("In the bottom row, the first place is 7, the second place is 8, and the third place is 9.")
print("All set? Ok, now let's play the game!")

#i made a fuction for assigning a letter to the user and assigning the computer a letter
def inputUserLetter(): 
    letter = ''
    #it will ask the user this question when they are not X or O, so it will ask when they haven't gotten a letter yet, (so at the beginning of the game) 
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        #it will make the input into an uppercase letter
        letter = input().upper()
        #if the letter is x the following happens
    if letter == 'X':
    # we start with x going first
        return ['X', 'O']
    else:
    #we start with o going first
        return ['O', 'X']
    
#i made a function to determine who goes first
def whoGoesFirst():
#if 0 is randomly chosen between 0 and 1 the computer goes first
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
    #if 1 is chosen then the user goes first
        return 'user'
    
#i made a fucntion to determine this is if they want to play again
def playAgain():
#it asks whether they want to play again or not
    print('Do you want to play again? (yes or no)')
    #if they say yes (which starts with y) they will play again
    return input().lower().startswith('y')

#i made the board (executed the function)
def makeMove(board, letter, move):
    board[move] = letter

#this defines the winner (making a function)
#bo-is abbreviation for bo
#le-is abbreviation for le
def isWinner(bo, le):
    return ((bo[1] == le and bo[2] == le and bo[3] == le) or # across the top
    (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle
    (bo[7] == le and bo[8] == le and bo[9] == le) or # across the bottom
    (bo[1] == le and bo[4] == le and bo[7] == le) or # down the left side
    (bo[2] == le and bo[5] == le and bo[8] == le) or # down the middle
    (bo[3] == le and bo[6] == le and bo[9] == le) or # down the right side
    (bo[1] == le and bo[5] == le and bo[9] == le) or # diagonal
    (bo[3] == le and bo[5] == le and bo[7] == le)) # diagonal

#I made a copy of the board
def getBoardCopy(board):
    dupeBoard = []
    for i in board:
        dupeBoard.append(i)
    return dupeBoard
#if the space is free they will be allowed to move there
def isSpaceFree(board, move):
    return board[move] == ' '
def getUserMove(board):
    move = ' '
    #when their move is not already in any of the places the can move there
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What is your move? (1-9)')
        move = input()
    return int(move)
#this is the computer randomly choosing a move from the left places
def chooseRandomMoveFromList(board, movesList):
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None
    
    #its a function for the computer actually moving somewhere
def getComputerMove(board, computerLetter):
#it tells the computer 
    if computerLetter == 'X':
        userLetter = 'O'
    else:
        userLetter = 'X'
        #computer has to pick a place between 1-10 b/c thats all there is
        #the rest below it is if the computer wins
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, userLetter, i)
            if isWinner(copy, userLetter):
                return i
            #if the space is free it will let the computer move there if not it wont go there
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move
    if isSpaceFree(board, 5):
        return 5
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])
#function for if the board is full (which automatically means that no one has won yet, becuase the winning function didn't kick in)
def isBoardFull(board):
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True
#this will happen at the beginning itwelcomes them to the tic tac toe game
print('Welcome to the Tic Tac Toe game!')
while True:
    theBoard = [' '] * 10
    userLetter, computerLetter = inputUserLetter()
    turn = whoGoesFirst()
    #it tells them who goes first
    print('The ' + turn + ' goes first.')
    gameIsPlaying = True
    #if the user wins
    while gameIsPlaying:
        if turn == 'user':
            drawBoard(theBoard)
            move = getUserMove(theBoard)
            makeMove(theBoard, userLetter, move)
            if isWinner(theBoard, userLetter):
                drawBoard(theBoard)
                print('Whoo! You won the game and you beat the computer!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'computer'
        #if the user didn't win
        else:
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)
            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print('The computer has beaten you! You lose!!')
                gameIsPlaying = False
            else:
            #if the board is full (calls on the function) it tells the user that the game is a tie
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'user'
                    #if the user is asked whether they want to play agin and they say no then we break the code, ending it so it doesn't loop and happen again and again
    if not playAgain():
        break
