# time optimization: iterative approach

class LongestCommonSubsequence:
  def memoization(self, s1, s2):
    N, M = len(s1), len(s2)
    cache = [[0] * (M+1) for _ in range(N+1)]

    for i1 in range(N):
      for i2 in range(M):
        if s1[i1] == s2[i2]:
          cache[i1+1][i2+1] = 1 + cache[i1][i2]
        else:
          cache[i1+1][i2+1] = max(cache[i1][i2+1], cache[i1+1][i2])

    return cache[N][M]


if __name__ == "__main__":
  lcs = LongestCommonSubsequence().memoization("adcb", "abc")
  print(lcs)