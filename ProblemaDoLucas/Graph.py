class Graph:
  def __init__(self):
    self.nodes = []
    self.edges = []

  def __str__(self):
    return "Graph\n Nodes:\t{nodes}\n Edges:\t{edges}" \
      .format(nodes=self.nodes, edges=self.edges)

  # Method for create nodes
  def addNode(self, node):
    self.nodes.append(node)

  # Method for create edges
  def addEdgesWithNodes(self, node1, node2):
    if node1 not in self.nodes:
      self.nodes.append(node1)
    if node2 not in self.nodes:
      self.nodes.append(node2)

    self.edges.append((node1, node2))

  # Method that return the adjacent nodes of a node
  def getAdjacentNodes(self, node):
    adjacentNodes = []
    for edges in self.edges:
      if node in edges:
        index = 0 if edges.index(node) else 1
        adjacentNodes.append(edges[index])

    return adjacentNodes

  # DFS Algorithm for search a goal from a root 
  # with a optional param for run some function
  # return the visited nodes
  def depthFirstSearch(self, searchRoot, goalNode, genEdges=None):
    visited = []
    frontier = []
    frontier.append(searchRoot)

    cameFrom = {}
    cameFrom[searchRoot] = None
    
    while frontier:
      currentNode = frontier.pop()
      visited.append(currentNode)
      if currentNode == goalNode:
        return self.getPathOf(currentNode, cameFrom, searchRoot)
      if genEdges:
        genEdges(self, currentNode)
      adjacentNodes = reversed(self.getAdjacentNodes(currentNode))
      for node in adjacentNodes:
        if (node not in visited) and (node not in frontier):
          frontier.append(node)
          cameFrom[node] = currentNode

    return None

  def getPathOf(self, node, cameFrom, initial):
    path = []
    current = node
    while current != initial:
        path.append(current)
        current = cameFrom[current]

    path.append(initial)
    path = list(reversed(path))
    return path