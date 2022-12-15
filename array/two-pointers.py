# algorithm: initial left pointer at begin and right pointer at the end 
#  then shift left, right pointer until answer is not get.


class TwoPointer:
  # check if the array is palindrome or not
  def isPalindrome(self, nums):
    l, r = 0, len(nums)-1

    while l < r:
      if nums[l] != nums[r]: 
        return False
      l += 1
      r -= 1

    return True

  # given a sorted input array, return the two indices of two telements which sum up to the target value,
  # assume there's exactly one solution.
  def targetSum(self, nums, target):
    l, r = 0, len(nums)-1

    while l < r:
      sum = nums[l] + nums[r]
      if sum < target:
        l += 1
      elif sum > target:
        r -= 1
      else:
        return True

    return False


if __name__ == "__main__":
  if TwoPointer().isPalindrome([1,2,3,3,2,1]):
    print("array is palindrome")
  if TwoPointer().targetSum([1,2,3,4], 7):
    print("values found with sum equal to target")