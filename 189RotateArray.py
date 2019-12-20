nums = [1, 2, 3, 4, 5, 6, 7]
k = 3


def rot(nums):
  nums[:] = nums[-k:] + nums[:-k]
  # for i, x in enumerate(res):
  # nums[i] = x


rot(nums)
print(nums)
