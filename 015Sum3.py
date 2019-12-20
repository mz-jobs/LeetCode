from itertools import combinations
nums = [-1, 0, 1, 2, -1, -4]


def threeSum(nums):

  res = set()
  nums.sort()

  for a in range(len(nums)-2):
    b = a+1
    c = len(nums)-1
    while b < c:
      S = nums[a] + nums[b] + nums[c]
      if S == 0:
        res.add((nums[a], nums[b], nums[c]))
      if S > 0:
        c -= 1
      else:
        b += 1

  return res


print(threeSum(nums))
