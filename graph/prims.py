import heapq

class Prim:
  def minimumSpanningTree(self, edges, n):
    adj = {}
    for i in range(1, n+1): 
      adj[i] = []
    for src, dst, weight in edges:
      adj[src].append((dst, weight))
      adj[dst].append((src, weight))

    minHeap = []
    for dst, weight in adj[1]:
      heapq.heappush(minHeap, (weight, 1, dst))
    
    visited = {1}
    mst = []
    while minHeap:
      weight, src, node = heapq.heappop(minHeap)
      if node in visited:
        continue

      mst.append((src,node))
      visited.add(node)
      for dst, w1 in adj[node]:
        if dst not in visited:
          heapq.heappush(minHeap, (w1, node, dst))
    return mst

if __name__ == "__main__":
  mst = Prim().minimumSpanningTree([[1,3,10], [3,4,1],[1,2,2],[2,4,5],[2,3,3]], 4)
  print(mst)
