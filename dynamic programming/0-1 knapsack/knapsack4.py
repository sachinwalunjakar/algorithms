# both space & time optimized: iterative approach

# true dynamic programming solution
class KnapSack:
  # time: O(N * M)
  # space: O(M)
  def memoization(self, profits, weights, capacity):
    N, M = len(profits), capacity

    cache = [0 for i in range(M+1)]

    for n in range(1, N):
      for m in range(M, -1, -1):
        skip = cache[m]
        include = 0
        if m - weights[n] >= 0:
          include = profits[n] + cache[m - weights[n]]

        cache[m] = max(skip, include)

    return cache[M]


if __name__ == "__main__":
  profit = KnapSack().memoization([4,4,7,1], [5,2,3,1], 8)
  print(profit)
