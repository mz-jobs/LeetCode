from functools import lru_cache
import sys
nums = [2, 3, 1, 1, 4]
# nums = [3, 2, 1, 0, 4]


reach = 0
i = 0
last = len(nums)-1
while i <= reach and reach < last:
  p = i + nums[i]
  if p > reach:
    reach = p
  i += 1

print(reach >= last)

# dp = [False] * len(nums)
# dp[0] = True
# for i in range(len(dp)):
#   if dp[i]:
#     for j in range(1, nums[i]+1):
#       if i+j < len(dp):
#         dp[i+j] = True
# print(dp[-1])

# def canJump(nums):
#   search = [0]
#   visited = set()

#   while search:
#     x = search.pop()
#     if x == len(nums)-1:
#       return True
#     for i in range(1, nums[x]+1):
#       if x+i < len(nums) and (x+i) not in visited:
#         search.append(x+i)
#         visited.add(x+i)
#   return False

# print(canJump([0, 1]))

# def canReachEnd(x):
#   if x >= len(nums):
#     return False
#   if x == len(nums)-1:
#     return True
#   for i in range(1, nums[x]+1):
#     if canReachEnd(x+i):
#       return True
#   return False

# print(canReachEnd(0))
