
class SlidingWindow:

  # find the length of the longest subarray, with same value in each position
  def longestSubarray(self, nums):
    l = 0
    maxLength = 0

    for r in range(len(nums)):
      if nums[l] != nums[r]:
        l = r
      maxLength = max(maxLength, r - l + 1)

    return maxLength

  
  # find the minimum length subarray, where the sum is greater than or equal to the target. Assume all values are positive.
  def minimumLengthSubarray(self, nums, target):
    l = 0
    minimumLength = float('inf')
    curSum = 0

    for r in range(len(nums)):
      curSum += nums[r]
      while curSum >= target and l < r:
        minimumLength = min(minimumLength, r-l+1)
        curSum -= nums[l]
        l += 1

    return minimumLength if minimumLength != float('inf') else 0
      

  



if __name__ == "__main__":
  slidingWindow = SlidingWindow()
  maxLength = slidingWindow.longestSubarray([4, 2, 2, 3, 3, 3])
  minimumLength = slidingWindow.minimumLengthSubarray([2, 3, 1, 2, 4, 3], 6)
  print(minimumLength)



