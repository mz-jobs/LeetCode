
coins = [1, 3, 4]
amount = 7

dp = [float('inf')] * (amount+1)
dp[0] = 0
for i in range(len(dp)):
  if dp[i] is not float('inf'):
    for c in coins:
      if i+c < len(dp) and dp[i]+1 < dp[i+c]:
        dp[i+c] = dp[i]+1

print(dp)
