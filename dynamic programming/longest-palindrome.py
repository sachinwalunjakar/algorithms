class LongestPalindrome:
  def longest(self, s): # 
    length = 0
    N = len(s)
    for i in range(N):
      length = max(length, self.helper(s, i, i))
      length = max(length, self.helper(s, i, i+1))
    return length
  
  # find max palindrome by expanding from middle
  # solve small problem first and use its result to solve bigger problem
  def helper(self, s, l, r): 
    length = 0
    while l >= 0 and r < len(s) and s[l] == s[r]:
      length = max(length, r-l + 1)
      l -= 1
      r += 1
    return length
  
  


if __name__ == "__main__":
  length = LongestPalindrome().longest("nitinopponi")
  print(length)


