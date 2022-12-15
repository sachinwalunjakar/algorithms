class TopologicalSort: # can be use if graph is undirected, asyclic
  def topologicalSort(self, edges: list, n: int, src: int):
    adj = {}
    for i in range(1, n+1):
      adj[i] = []
    for s, d in edges:
      adj[s].append(d)

    tsort = []
    visited = set()
    self.helperDFS(src, adj, visited, tsort)
    tsort.reverse()
    return tsort
    
  # posorder dfs
  def helperDFS(self, src, adj, visited, tsort):
    if src in visited:
      return
    
    visited.add(src)

    for neighbour in adj[src]:
      self.helperDFS(neighbour, adj, visited, tsort)

    tsort.append(src)



class TopologicalSortWithOutSrcGiven:
  def topologicalSort(self, edges: list, n: int):
    adj = {}
    for i in range(1, n+1):
      adj[i] = []
    for s, d in edges:
      adj[s].append(d)

    tsort = []
    visited = set()
    path = set()

    for node in range(1, n+1):
      graphContainCycle = not self.helperDFS(node, adj, visited, path, tsort)
      if graphContainCycle:
        print("cannot find topological sort, graph contain cycle")
    tsort.reverse()
    return tsort


  def helperDFS(self, src: int, adj: dict, visited: set, path: set, tsort: list) -> bool:
    if src in path:
      print(f"{src} is in path")
      return False
    if src in visited:
      return True
    
    path.add(src)
    visited.add(src)

    for neighbour in adj[src]:
      self.helperDFS(neighbour, adj, visited, path, tsort)

    path.remove(src)
    tsort.append(src)

    return True


if __name__ == "__main__":
  edges = [[1,3], [4,3],[1,2],[2,4],[2,3]]
  nodeCount = 4
  tsort = TopologicalSortWithOutSrcGiven().topologicalSort(edges, nodeCount)
  print(tsort)

    
    


