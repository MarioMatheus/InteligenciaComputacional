from Graph import Graph
from State import State
from StateHandler import StateHandler

# Creating the data structure and your handler
grafo = Graph()
stateHandler = StateHandler()

# Defining the initial state and the goal
initialState = State()              # State(board=[">",">",">",">"," ","<","<","<","<"])
goalState = stateHandler.goalState  # State(board=["<","<","<","<"," ",">",">",">",">"])
grafo.addNode(initialState)

# Method that will run inside the search for generates the possible states
def generateNextMoves(graph, state):
  pStates = stateHandler.nextPossibleStates(state)
  for pState in pStates:
    graph.addEdgesWithNodes(state, pState)

# Running the dfs
print(grafo.depthFirstSearch(initialState, goalState, generateNextMoves))
