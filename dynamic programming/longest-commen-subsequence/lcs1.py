# no optimization

class LongestCommonSubsequence:
  # time: O(2^n)
  def dfs(self, s1, s2): # return length of "longest common subsequence"
    return self.dfsHelper(s1, s2, 0, 0)

  def dfsHelper(self, s1, s2, i1, i2):
    if i1 == len(s1) or i2 == len(s2):
      return 0

    if s1[i1] == s2[i2]:
      return 1 + self.dfsHelper(s1, s2, i1+1, i2+1)
    
    return max(self.dfsHelper(s1, s2, i1+1, i2) , self.dfsHelper(s1, s2, i1, i2+1))




if __name__ == "__main__":
  lcs = LongestCommonSubsequence().dfs("adcb", "abc")
  print(lcs)
  