from copy import copy

class State:
  def __init__(self, missionaries=(3,0), cannibals=(3,0), boat='left'):
    self.missionaries = missionaries
    self.cannibals = cannibals
    self.boat = boat

  def __str__(self):
    return ("\nState:\n"
     " Missionaries - Left: {misLeft} | Right: {misRight}\n"
     " Cannibals - Left {canLeft} | Right {canRight}\n"
     " Boat on {boatPos}").format(
       misLeft=self.missionaries[0], misRight=self.missionaries[1],
       canLeft=self.cannibals[0], canRight=self.cannibals[1],
       boatPos=self.boat)

  def __eq__(self, rightState):
    return self.missionaries == rightState.missionaries \
      and self.cannibals == rightState.cannibals \
      and self.boat == rightState.boat

  def __repr__(self):
    return str(self)

  # Checks for more cannibals than missionaries
  def killingsHappen(self):
    return (self.missionaries[0] != 0 and self.missionaries[0] < self.cannibals[0])\
      or (self.missionaries[1] != 0 and self.missionaries[1] < self.cannibals[1])

  # Moves the boat from one shore to the other if possible
  def moveBoat(self, qtdMissionarios, qtdCannibals):
    qtdOnBoat = qtdMissionarios + qtdCannibals
    if not(0 < qtdOnBoat < 3):
      return False
    if self.boat == 'left':
      if self.missionaries[0] < qtdMissionarios or self.cannibals[0] < qtdCannibals:
        return False
      self.missionaries = (self.missionaries[0] - qtdMissionarios, self.missionaries[1] + qtdMissionarios)
      self.cannibals = (self.cannibals[0] - qtdCannibals, self.cannibals[1] + qtdCannibals)
      self.boat = 'right'
    else:
      if self.missionaries[1] < qtdMissionarios or self.cannibals[1] < qtdCannibals:
        return False
      self.missionaries = (self.missionaries[0] + qtdMissionarios, self.missionaries[1] - qtdMissionarios)
      self.cannibals = (self.cannibals[0] + qtdCannibals, self.cannibals[1] - qtdCannibals)
      self.boat = 'left'
    return True

class StateHandler:

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
