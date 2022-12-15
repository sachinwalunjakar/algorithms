class Combinations:
  # return all position combination of numbers from '1 to n' with size 'k'
  def combinations(self, n, k):
    curset, combs = [], []
    self.helper2(0, n, k, curset, combs)
    return combs
    
  # time: O(k * 2^n) 
  # decision: include or not include number
  def helper1(self, i, n, k, curset, combs):
    if len(curset) == k:
      combs.append(curset.copy())
      return 
    
    if i >= n:
      return 

    curset.append(i)
    self.helper1(i + 1, n, k, curset, combs)
    
    curset.pop()
    self.helper1(i + 1, n, k, curset, combs)
    

  # time: O(k * C(n, k))
  # decision: fill current spot with number
  def helper2(self, i, n, k, curset, combs):
    if len(curset) == k:
      combs.append(curset.copy())
    
    if i >= n:
      return
    
    for j in range(i, n+1):
      curset.append(j)
      self.helper2(j+1, n, k, curset, combs)
      curset.pop()



if __name__ == "__main__":
  c = Combinations().combinations(4, 2)
  print(c)

