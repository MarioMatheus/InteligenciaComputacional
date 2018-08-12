class Node:
  def __init__(self, content):
    self.content = content

  def __str__(self):
    return str(self.content)

  def __repr__(self):
    return str(self)

  def __eq__(self, rightNode):
    return self.content == rightNode.content


class Graph:
  def __init__(self):
    self.nodes = []
    self.edges = []

  def __str__(self):
    return "Graph\n Nodes:\t{nodes}\n Edges:\t{edges}".format(nodes=self.nodes, edges=self.edges)

  def addNode(self, node):
    self.nodes.append(node)

  def addEdgesWithNodes(self, node1, node2):
    if node1 not in self.nodes:
      self.nodes.append(node1)
    if node2 not in self.nodes:
      self.nodes.append(node2)

    self.edges.append((node1, node2))

  def getAdjacentNodes(self, node):
    adjacentNodes = []
    for edges in self.edges:
      if node in edges:
        index = 0 if edges.index(node) else 1
        adjacentNodes.append(edges[index])

    return adjacentNodes

  def depthFirstSearch(self, searchRoot, goalNode, genNode=None):
    visited = []
    frontier = []
    frontier.append(searchRoot)
    while frontier:
      currentNode = frontier.pop()
      if currentNode == goalNode:
        visited.append(currentNode)
        return visited
      visited.append(currentNode)
      if genNode:
        genNode(self, currentNode)
      adjacentNodes = reversed(self.getAdjacentNodes(currentNode))
      for node in adjacentNodes:
        if (node not in visited) and (node not in frontier):
          frontier.append(node)

    return None
