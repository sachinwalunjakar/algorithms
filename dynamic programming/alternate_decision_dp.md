# Alternate Decision DP


**Problem**: 309. Best Time to Buy and Sell Stock with Cooldown

Solution:
- Decision at each step: 
  1. **buy/sell**  (alternate decision if stock bought then decision is "**sell or cooldown**" if selled then first **cooldown** then "**buy or cooldown**")
  2. **cooldown**

- Code:
```cpp
class Solution {
public:
  int maxProfit(vector<int>& prices) {
    vector<vector<int>> cache(2, vector<int>(prices.size(), -1));
    return dfs(prices, 0, true, cache);
  }
  
  int dfs(vector<int>& prices, int i, bool isbuying, vector<vector<int>>& cache) {
    if(i >= prices.size()) return 0;
    if(cache[isbuying][i] != -1) return cache[isbuying][i];

    if(isbuying) {
      int buy = dfs(prices, i+1, !isbuying, cache) - prices[i]; // buy
      int cooldown = dfs(prices, i+1, isbuying, cache); // cooldown
      cache[isbuying][i] = max(buy, cooldown);
      return max(buy, cooldown);
    } 
    else {
      int sell = dfs(prices, i+2, !isbuying, cache) + prices[i]; // sell
      int cooldown = dfs(prices, i+1, isbuying, cache); // cooldown
      cache[isbuying][i] = max(sell, cooldown);
      return max(sell, cooldown);
    }
  }
};
```
