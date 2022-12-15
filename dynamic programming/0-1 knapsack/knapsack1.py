# no optimization

class KnapSack: # 0/1 knapsack
  # time: O(2^n)
  # space: O(1)
  def dfs(self, profits: list, weights: list, capacity: int) -> int:
    return self.helper(0, profits, weights, capacity)


  def helper(self, i: int, profits: list, weights: list, capacity: int) -> int:
    if i == len(profits):
      return 0

    # skip item
    maxProfit = self.helper(i+1, profits, weights, capacity) 

    # include item
    newCap = capacity - weights[i]
    if newCap > 0:
      p = profits[i] + self.helper(i+1, profits, weights, newCap)
      maxProfit = max(maxProfit, p)

    return  maxProfit



if __name__ == "__main__":
  profit = KnapSack().dfs(profits=[4,4,7,1], weights=[5,2,3,1], capacity=8)
  print(profit)

