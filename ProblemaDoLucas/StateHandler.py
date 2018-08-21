from copy import deepcopy

class StateHandler:

  def nextPossibleStates(self, state):
    possibleStates = []

    for index, _ in enumerate(state.board):
      if state.isPossibleMove(index):
        auxState = deepcopy(state)
        auxState.moveArrow(index)
        possibleStates.append(auxState)

    return possibleStates  