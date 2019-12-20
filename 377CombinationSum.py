from itertools import product, permutations
nums = [1, 2, 3]
target = 4

dp = [0] * (target+1)
dp[0] = 1

for i in range(target):
  if dp[i] == 0:
    continue
  for n in nums:
    if i+n <= target:
      dp[i+n] += dp[i]

print(dp)
