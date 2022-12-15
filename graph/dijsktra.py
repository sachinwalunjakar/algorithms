import heapq

class Dijkstra:
  def shortestPath(self, edges, n, src):
    adj = {}
    for i in range(1, n+1):
      adj[i] = []
    for s, d, w in edges:
      adj[s].append((d, w))
    
    shortest = {}
    minHeap = [(0, src)]

    while minHeap:
      w, n = heapq.heappop(minHeap)
      if n in shortest:
        continue
      shortest[n] = w

      for d, w1 in adj[n]:
        if d not in shortest:
          heapq.heappush(minHeap, (w1 + w, d))

    return shortest


      
if __name__ == "__main__":
  nodes = Dijkstra().shortestPath([[1,3,10], [3,4,1],[1,2,2],[2,4,5],[2,3,3]], 4, 1)
  print(nodes)


