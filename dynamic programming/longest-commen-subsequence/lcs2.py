# time optimization: recursive approach

class LongestCommonSubsequence:
  # time: O(N*M)
  def memoization(self, s1, s2): # return length of "longest common subsequence"
    N, M = len(s1), len(s2)
    cache = [[-1] * (M) for i in range(N)]

    return self.memoHelper(s1, s2, 0, 0, cache)


  def memoHelper(self, s1, s2, i1, i2, cache):
    if i1 == len(s1) or i2 == len(s2):
      return 0

    if cache[i1][i2] != -1:
      return cache[i1][i2]
    
    if s1[i1] == s2[i2]:
      cache[i1][i2] = 1 + self.memoHelper(s1, s2, i1+1, i2+1, cache)
    else:
      cache[i1][i2] = max(self.memoHelper(s1, s2, i1+1, i2, cache) , self.memoHelper(s1, s2, i1, i2+1, cache))
    
    return cache[i1][i2]


if __name__ == "__main__":
  lcs = LongestCommonSubsequence().memoization("adcb", "abc")
  print(lcs)
  