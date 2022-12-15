class Permutation:
  # return all position permutation of array
  def permutation(self, nums):
    perms = [[]]
    return self.helper1(0, nums, perms)
    

  # time: O(n^2 * n!)
  # --------------- wrong output: correction is needed ---------------
  def helper1(self, i, nums, perms): # recursive approach
    if i == len(nums):
      return perms 

    newPerms = []
    for p in perms:
      for j in range(0, len(p)+1): # insert num[i] to all position in permutation
        pCopy = p.copy()
        pCopy.insert(j, nums[i])
        newPerms.append(pCopy)
    perms = newPerms

    return self.helper1(i+1, nums, perms)

  # time: O(n^2 * n!)
  def helper2(self, nums): # iterative approach
    perms = [[]]

    for i in range(len(nums)):
      newPerms = []
      for p in perms:
        for j in range(0, len(p)+1):
          pcopy = p.copy()
          pcopy.insert(j, nums[i])
          newPerms.append(pcopy)
      perms = newPerms

    return perms

if __name__ == "__main__":
  p = Permutation().permutation([1, 2, 3])
  print(p)







