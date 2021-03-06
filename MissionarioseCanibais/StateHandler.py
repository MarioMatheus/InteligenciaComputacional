from copy import copy
from State import State

class StateHandler:
  def __init__(self):
      self.goalState = State((0,3),(0,3),'right')

  # Generates the possible states from a state
  def nextPossibleStates(self, state):
    possibleStates = []

    # Move two missionaries if possible
    auxState = copy(state)
    if auxState.moveBoat(2,0) and not auxState.killingsHappen():
      possibleStates.append(auxState)

    # Move two cannibals if possible
    auxState = copy(state)
    if auxState.moveBoat(0,2) and not auxState.killingsHappen():
      possibleStates.append(auxState)

    # Move one cannibal and one missionary if possible
    auxState = copy(state)
    if auxState.moveBoat(1,1) and not auxState.killingsHappen():
      possibleStates.append(auxState)

    # Move one missionary if possible
    auxState = copy(state)
    if auxState.moveBoat(1,0) and not auxState.killingsHappen():
      possibleStates.append(auxState)

    # Move one cannibal if possible
    auxState = copy(state)
    if auxState.moveBoat(0,1) and not auxState.killingsHappen():
      possibleStates.append(auxState)

    return possibleStates
