# Constants for represent the shore
LEFT = 0    # Left Shore
RIGHT = 1   # Right Shore

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
       misLeft=self.missionaries[LEFT], misRight=self.missionaries[RIGHT],
       canLeft=self.cannibals[LEFT], canRight=self.cannibals[RIGHT],
       boatPos=self.boat)

  def __hash__(self):
      return super().__hash__()

  def __eq__(self, rightState):
    return self.missionaries == rightState.missionaries \
      and self.cannibals == rightState.cannibals \
      and self.boat == rightState.boat

  def __repr__(self):
    return str(self)

  # Checks for more cannibals than missionaries
  def killingsHappen(self):
    return (self.missionaries[LEFT] != 0 and self.missionaries[LEFT] < self.cannibals[LEFT])\
      or (self.missionaries[RIGHT] != 0 and self.missionaries[RIGHT] < self.cannibals[RIGHT])

  # Moves the boat from one shore to the other if possible
  def moveBoat(self, qtdMissionarios, qtdCannibals):
    qtdOnBoat = qtdMissionarios + qtdCannibals
    if not(0 < qtdOnBoat < 3):
      return False
    if self.boat == 'left':
      if self.missionaries[LEFT] < qtdMissionarios or self.cannibals[LEFT] < qtdCannibals:
        return False
      self.missionaries = (self.missionaries[LEFT] - qtdMissionarios, self.missionaries[RIGHT] + qtdMissionarios)
      self.cannibals = (self.cannibals[LEFT] - qtdCannibals, self.cannibals[RIGHT] + qtdCannibals)
      self.boat = 'right'
    else:
      if self.missionaries[RIGHT] < qtdMissionarios or self.cannibals[RIGHT] < qtdCannibals:
        return False
      self.missionaries = (self.missionaries[LEFT] + qtdMissionarios, self.missionaries[RIGHT] - qtdMissionarios)
      self.cannibals = (self.cannibals[LEFT] + qtdCannibals, self.cannibals[RIGHT] - qtdCannibals)
      self.boat = 'left'
    return True
