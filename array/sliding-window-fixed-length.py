class SlidingWindow:

  # given an array, return true if there are two elements within a window of size k that are equal
  def closeDublicate(self, nums, k): 
    window = set()
    l = 0

    for r in range(len(nums)):
      if r-l >= k:
        window.remove(nums[l])
        l += 1
      if nums[r] in window:
        return True
      window.add(nums[r])
    return False



if __name__ == "__main__":
  if SlidingWindow().closeDublicate([1,2,3,2,3,3], 2):
    print("window found")
  else:
    print("window not exist")

