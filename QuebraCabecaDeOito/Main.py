from Graph import Graph
from State import State
from StateHandler import StateHandler

# Creating the data structure and your handler
grafo = Graph()
stateHandler = StateHandler()

# Defining the initial state and the goal
initialState = State([[' ','2','3'],['1','4','5'],['7','8','6']])
goalState = stateHandler.goalState
grafo.addNode(initialState)

# Method that will run inside the search for generates the possible states
def generateNextMoves(graph, state):
  pStates = stateHandler.nextPossibleStates(state)
  for pState in pStates:
    graph.addEdgesWithNodes(state, pState)


def popBestStateWithManhattanDistance(frontier):
  bestState = frontier[0]
  for state in frontier:
    if stateHandler.manhattanDistance(state) < stateHandler.manhattanDistance(bestState):
      bestState = state

  return frontier.pop(frontier.index(bestState))
      

# Running the A*
print(grafo.aStar(initialState, goalState, popBestStateWithManhattanDistance, generateNextMoves))
