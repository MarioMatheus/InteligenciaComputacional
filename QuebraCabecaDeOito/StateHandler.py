from State import State
from copy import deepcopy

class StateHandler:
  def __init__(self):
      self.goalState = State([['1','2','3'],['4','5','6'],['7','8',' ']])
      self.goalMap = self.mappingGoal()


  def mappingGoal(self):
    goalMap = {}
    
    for i, row in enumerate(self.goalState.board):
      for j, value in enumerate(row):
        if value is not ' ':
          goalMap[value] = (i,j)

    return goalMap

  
  def manhattanDistance(self, state):
    manhattanDistance = 0

    for key, value in self.goalMap.items():
      for i, row in enumerate(state.board):
        if key in row:
          (indexRow, indexCol) = (i, row.index(key))
          manhattanDistance += abs(value[0] - indexRow) + abs(value[1] - indexCol)

    return manhattanDistance


  def nextPossibleStates(self, state):
    possibleStates = []

    for i, _ in enumerate(state.board):
      for j, _ in enumerate(state.board):
        if state.isValidMove(i,j):
          auxState = deepcopy(state)
          auxState.movePiece(i,j)
          possibleStates.append(auxState)

    return possibleStates


