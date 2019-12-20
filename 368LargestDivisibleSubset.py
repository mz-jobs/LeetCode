from typing import List
nums = [1, 2, 4, 8, 10]


solutions = []


def walk(subset, i):
  if i == len(nums):
    solutions.append(subset)
    return
  if len(subset) == 0 or nums[i] % subset[-1] == 0:
    walk(subset + [nums[i]], i+1)

  walk(subset, i+1)


walk([], 0)
print(solutions)


def largestDivisibleSubset(nums: List[int]) -> List[int]:
  if not nums:
    return []

  nums.sort()
  dp = [[] for _ in range(len(nums))]
  # print(dp)

  best = []
  for i in range(len(nums)):
    dp[i].append(nums[i])
    for j in range(i+1, len(nums)):
      if nums[j] % nums[i] == 0 and len(dp[i]) > len(dp[j]):
        dp[j] = dp[i].copy()
    if len(dp[i]) > len(best):
      best = dp[i]
  # print(dp)
  # return max(dp, key=len)
  return best


x = largestDivisibleSubset(nums)
print(x)
