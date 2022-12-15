# time optimized: iterative approach

class KnapSack:
  # time & space : O(N * M)
  def memoization(self, profits, weights, capacity):
    # 2d array with N rows, M columns
    N, M = len(profits), capacity
    cache = [[0] * (M+1) for i in range(N)]

    for m in range(M):
      if m - weights[0] >=0:
        cache[0][m] = profits[0]

    for n in range(1, N):
      for m in range(M+1):
        skip = cache[n-1][m]
        include = 0
        if m - weights[n] >=0:
          include = profits[n] + cache[n-1][m-weights[n]]

        cache[n][m] = max(skip, include)

    return cache[N-1][M]


if __name__ == "__main__":
  profit = KnapSack().memoization([4,4,7,1], [5,2,3,1], 8)
  print(profit)







