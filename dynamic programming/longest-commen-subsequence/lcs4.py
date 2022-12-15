# both time & space optimization

class LongestCommonSubsequence:
  # time: O(N*M) 
  # space: O(M)
  def memoization(self, s1, s2):

    N, M = len(s1), len(s2)

    cache = [0] * (M+1)

    for i1 in range(N):
      newCache = [0] * (M+1)
      for i2 in range(M):
        if s1[i1] == s2[i2]:
          newCache[i2+1] = 1 + cache[i2]
        else:
          newCache[i2+1] = max(cache[i2+1], newCache[i2])
      cache = newCache
    
    return cache[M]


if __name__ == "__main__":
  lcs = LongestCommonSubsequence().memoization("adcd", "abc")
  print(lcs)
    

    