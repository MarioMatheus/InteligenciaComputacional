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
      self.board = self.shuffleBoard()
    


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


  def countDegreeOfDisorder(self, board):
    count = 0
    correctMap = {
      '1': (0,0), '2': (0,1), '3': (0,2),
      '4': (1,0), '5': (1,1), '6': (1,2),
      '7': (2,0), '8': (2,1)
    }
    for i, row in enumerate(board):
      for j, value in enumerate(row):
        if value is not ' ':
          correctPos = correctMap[value]
          if i is not correctPos[0] or j is not correctPos[1]:
            count += 1
    
    return count

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

  
  def isValidMove(self, indexRow, indexCol):
    return (abs(indexRow - self.emptySpaceIndexes[0]) + 
      abs(indexCol - self.emptySpaceIndexes[1])) is 1
      
  
  def movePiece(self, indexRow, indexCol):
    (self.board[self.emptySpaceIndexes[0]][self.emptySpaceIndexes[1]]), (self.board[indexRow][indexCol]) = \
    (self.board[indexRow][indexCol]), (self.board[self.emptySpaceIndexes[0]][self.emptySpaceIndexes[1]])

    self.emptySpaceIndexes = (indexRow, indexCol)

