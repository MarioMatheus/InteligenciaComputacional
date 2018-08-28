from random import randint
from copy import copy

class State:
  def __init__(self, board=None):
    self.emptySpaceIndexes = (2,2)
    
    if board is not None:
      self.board = board
      for row in self.board:
        if ' ' in row:
          self.emptySpaceIndexes = (self.board.index(row), row.index(' '))
    else:
      self.board = self.generateSolvableBoard()
    


  def __eq__(self, rightValue):
      return self.board == rightValue.board

  
  def __repr__(self):
      return str(self)


  def __str__(self):
      return ("\nBoard:\n"
      "\t{a11}  {a12}  {a13}\n"
      "\t{a21}  {a22}  {a23}\n"
      "\t{a31}  {a32}  {a33}\n").format(
        a11=self.board[0][0], a12=self.board[0][1], a13=self.board[0][2],
        a21=self.board[1][0], a22=self.board[1][1], a23=self.board[1][2],
        a31=self.board[2][0], a32=self.board[2][1], a33=self.board[2][2]
      )


  def getListOfPieces(self, board):
    listOfPieces = []
    for row in board:
      for value in row:
        listOfPieces.extend(value)
    
    return listOfPieces



  def checkIfBoardIsSolvable(self, board):
    inversions = 0
    auxList = self.getListOfPieces(board)
    
    for i in range(len(auxList)):
      for j in range(i+1, len(auxList)):
        if auxList[j] is not ' ' and auxList[i] is not ' ' and auxList[j] > auxList[i]:
          inversions += 1
    
    return (inversions%2 == 0)


  def shuffleBoard(self):
    board = []
    numbers = ['1','2','3','4','5','6','7','8']

    for i in range(3):
      board.append([
        numbers.pop(randint(0, len(numbers)-1)),
        numbers.pop(randint(0, len(numbers)-1)),
        numbers.pop(randint(0, len(numbers)-1)) if i is not 2 else ' '
      ])
    
    return board


  def generateSolvableBoard(self):
    auxBoard = self.shuffleBoard()
    while not self.checkIfBoardIsSolvable(auxBoard):
      auxBoard = self.shuffleBoard()

    return auxBoard
    

  
  def isValidMove(self, indexRow, indexCol):
    return (abs(indexRow - self.emptySpaceIndexes[0]) + 
      abs(indexCol - self.emptySpaceIndexes[1])) is 1
      
  
  def movePiece(self, indexRow, indexCol):
    (self.board[self.emptySpaceIndexes[0]][self.emptySpaceIndexes[1]]), (self.board[indexRow][indexCol]) = \
    (self.board[indexRow][indexCol]), (self.board[self.emptySpaceIndexes[0]][self.emptySpaceIndexes[1]])

    self.emptySpaceIndexes = (indexRow, indexCol)

