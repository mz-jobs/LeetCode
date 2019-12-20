# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
# If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
# The replacement must be in-place and use only constant extra memory.
# Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1

#  go from right to find a decreasing step
#  0 4 5 3 2 1
#    ^ ^ first decreasing pair
# swap
# 0 5 4 3 2 1
#     ^ ------
# and flip the rest to the right
# 0 5 1 2 3 4


import typing


class Solution:
  def nextPermutation(self, nums: typing.List[int]) -> None:
    """
      Do not return anything, modify nums in-place instead.
    """
    i = len(nums)-1
    while (i > 0) and (nums[i-1] >= nums[i]):
      i = i-1

    if i > 0:   # if not at the end
      jmin = i  # find lowest among that is higher than a[i-1]
      j = i+1
      while j < len(nums):
        if (nums[j] > nums[i-1]) and (nums[j] <= nums[jmin]):
          jmin = j
        j = j+1
      nums[i-1], nums[jmin] = nums[jmin], nums[i-1]  # swap

    j = len(nums)-1
    # flip right
    while i < j:
      nums[i], nums[j] = nums[j], nums[i]
      j = j-1
      i = i+1


nums = [4, 5, 3, 2, 1]
nums = [1, 2, 0, 3]
nums = [1, 3, 2]
nums = [0, 3, 2, 1]
nums = [5, 1, 1]
nums = [5, 4, 7, 5, 3, 2]
nums = [2, 3, 1, 3, 3]

Solution().nextPermutation(nums)
print(nums)
