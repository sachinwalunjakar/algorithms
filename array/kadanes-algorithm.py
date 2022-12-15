# algorithm: increment right pointer until condition satified, once condition not satified then
#  make size of window zero by move left to position of right.


class Kadanes:
  # find non-empty sub-array with max sum
  def kadanes(self, nums):
    maxSum = nums[0]
    curSum = 0
    for n in nums:
      curSum = max(curSum, 0) 
      curSum += n
      maxSum = max(maxSum, curSum)
    return maxSum

      
if __name__ == "__main__":
  maxSum = Kadanes().kadanes([4, -1, 2, -7, 3, 4])
  print(maxSum)