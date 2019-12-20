
# days = [1, 4, 6, 7, 8, 20]
days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31]
costs = [2, 7, 15]


N = 365
days = set(days)
dp = [float('inf')] * (N+1)
dp[0] = 0

for i in range(len(dp)-1):
  if i+1 in days:
    if i+1 < len(dp) and dp[i] + costs[0] < dp[i+1]:
      dp[i+1] = dp[i]+costs[0]

    if i+7 < len(dp) and dp[i] + costs[1] < dp[i+7]:
      dp[i+7] = dp[i]+costs[1]

    if i+30 < len(dp) and dp[i] + costs[2] < dp[i+30]:
      dp[i+30] = dp[i]+costs[2]
  else:
    if dp[i] < dp[i+1]:
      dp[i+1] = dp[i]

print(dp)
