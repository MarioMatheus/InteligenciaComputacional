class State:
  def __init__(self, board=[">",">",">",">"," ","<","<","<","<"]):
      self.board = board
      self.emptyFieldIndex = self.board.index(" ")

  def __eq__(self, rightState):
      return self.board == rightState.board

  def __str__(self):
      return "\nBoard: " + str(self.board)
  
  def __repr__(self):
      return str(self)


  # Move the arrow to the empty space
  def moveArrow(self, arrowIndex):
    self.board[self.emptyFieldIndex], self.board[arrowIndex] = \
    self.board[arrowIndex], self.board[self.emptyFieldIndex]

    self.emptyFieldIndex = arrowIndex


  # Check if is possible to move the arrow
  def isPossibleMove(self, arrowIndex):
    differenceOfEmptySpace = self.emptyFieldIndex - arrowIndex

    if self.board[arrowIndex] is ">" and differenceOfEmptySpace > 0:
      if (differenceOfEmptySpace is 2 and self.board[arrowIndex+1] is "<") or differenceOfEmptySpace is 1:
        return True

    if self.board[arrowIndex] is "<" and differenceOfEmptySpace < 0:
      if (differenceOfEmptySpace is -2 and self.board[arrowIndex-1] is ">") or differenceOfEmptySpace is -1:
        return True

    return False

