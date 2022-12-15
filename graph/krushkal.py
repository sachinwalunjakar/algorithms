import heapq
from _util import UnionFind


class Krushkal:
  def minimumSpanningTree(self, edges, n):
    minHeap = []
    for src, dst, weight in edges:
      heapq.heappush(minHeap, (weight, src, dst))
    
    visited = {}
    unionFind = UnionFind(n)
    mst = []
    while minHeap:
      weight, src, dst = heapq.heappop(minHeap)
      if not unionFind.union(src, dst):
        continue
      mst.append((src, dst))
    return mst


if __name__ == "__main__":
  mst = Krushkal().minimumSpanningTree([[1,3,10], [3,4,1],[1,2,2],[2,4,5],[2,3,3]], 4)
  print(mst)


