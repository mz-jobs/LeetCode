nums = [2, 7, 9, 3, 1]
nums = []

dp = [0] * (len(nums)+3)


for i in range(len(nums)-1, -1, -1):
  dp[i] = nums[i] + max(dp[i+2], dp[i+3])

print(max(dp[0], dp[1]))
