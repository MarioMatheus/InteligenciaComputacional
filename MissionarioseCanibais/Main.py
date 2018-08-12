from GraphHandler import Graph
from State import State, StateHandler

grafo = Graph()
stateHandler = StateHandler()

initialState = State()
goalState = State((0,3),(0,3),'right')
# print(initialState)
# print(goalState)

grafo.addNode(initialState)

def generateNextMoves(graph, state):
  # graph.addEdgesWithNodes(state, State((0,3),(0,3),'right'))
  pStates = stateHandler.nextPossibleStates(state)
  for pState in pStates:
    graph.addEdgesWithNodes(state, pState)


print(grafo.depthFirstSearch(initialState, goalState, generateNextMoves))
