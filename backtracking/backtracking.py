class Subset:

  def getAllSubsets(self, nums):
    curset, subsets = [], []
    self.helper1(0, nums, curset, subsets)
    return subsets


  # get subsets with dublicates
  def helper1(self, i, nums, curset, subsets):
    if i >= len(nums):
      subsets.append(curset.copy())
      return
    
    # decision to include nums[i]
    curset.append(nums[i])
    self.helper1(i+1, nums, curset, subsets)

    # decision to NOT include nums[i]
    curset.pop()
    self.helper1(i+1, nums, curset, subsets)


  # get subsets without dublicates
  def helper2(self, i, nums, curset, subsets):
    if i >= len(nums):
      subsets.append(curset.copy())
      return 

    # decision to include nums[i] and any of its upcoming dublicate
    curset.append(nums[i])
    self.helper2(i + 1, nums, curset, subsets)

    # decision to NOT include nums[i] and any of its upcoming dublicate
    curset.pop()
    while(i+1 < len(nums) and nums[i] == nums[i+1]):
      i += 1
    self.helper2(i + 1, nums, curset, subsets)



if __name__ == "__main__":
  s = Subset()
  print(s.getAllSubsets([1, 2, 2, 3]))


