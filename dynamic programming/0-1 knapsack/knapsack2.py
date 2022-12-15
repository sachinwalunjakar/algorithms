# time optimized: recursive approach

class KnapSack:
  # time & space : O(N * M)
  def memoization(self, profit, weight, capacity):
    # 2d array with N rows, M columns
    N, M = len(profit), capacity
    cache = [[-1] * (M+1) for i in range(N)]

    profit = self.memoHelper(0, profit, weight, capacity, cache)
    return profit


  def memoHelper(self, i, profits, weight, capacity, cache):
    if i >= len(profits):
      return 0
    if cache[i][capacity] != -1: # using cached result
      return cache[i][capacity]

    # skip item
    maxProfit = self.memoHelper(i+1, profits, weight, capacity, cache)

    # include item
    profit = 0
    if capacity - weight[i] >=0:
      profit = profits[i] + self.memoHelper(i+1, profits, weight, capacity-weight[i], cache)

    maxProfit = max(profit, maxProfit)
    cache[i][capacity] = profit # caching result
    
    return maxProfit
    
  
if __name__ == "__main__":
  profit = KnapSack().memoization([4,4,7,1], [5,2,3,1], 8)
  print(profit)


