class UnBoundedKnapSack:
  # time: O(N*M)
  def memoization(self, profits, weights, capacity):
    N, M = len(profits), capacity
    cache = [[-1] * (M+1) for i in range(N)]
    return self.memoHelper(0, profits, weights, capacity, cache)


  def memoHelper(self, i, profits, weights, capacity, cache):
    if i == len(profits):
      return 0
    if cache[i][capacity] != -1: # using cached result
      return cache[i][capacity]
    
    # skip item
    skip = self.memoHelper(i+1, profits, weights, capacity, cache)

    # include item
    include = 0
    if capacity - weights[i] >=0:
      include = profits[i] + self.memoHelper(i, profits, weights, capacity - weights[i], cache)

    maxProfit = max(skip, include)
    cache[i][capacity] = maxProfit # caching result

    return maxProfit

  # space & time optimized solution
  # time: O(N*M)  and  space: O(M)
  def maximumProfit(self, profits, weights, capacity):
    N, M = len(profits), capacity

    cache = [0] * (M+1)

    for n in range(1, N):
      for m in range(M+1):
        # skip item
        skip = cache[m] # profit by excluding item
        #include item
        include = 0
        if m - weights[n] >= 0:
          include = profits[n] + cache[m - weights[n]] # profit by including item

        cache[m] = max(skip, include) # caching result

    return cache[M]
    
        

if __name__ == "__main__":
  profit = UnBoundedKnapSack().maximumProfit([4,4,7,1], [5,2,3,1], 8)
  print(profit)
  

