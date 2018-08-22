from copy import deepcopy
from State import State

class StateHandler:
  def __init__(self):
      self.goalState = State(["<","<","<","<"," ",">",">",">",">"])

  def nextPossibleStates(self, state):
    possibleStates = []

    for index, _ in enumerate(state.board):
      if state.isPossibleMove(index):
        auxState = deepcopy(state)
        auxState.moveArrow(index)
        possibleStates.append(auxState)

    return possibleStates