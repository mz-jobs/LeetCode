s = "226"
s = "22"


if len(s) < 2:
  return len(s)

dp = [0]*len(s)
dp[0] = 1
dp[1] = 1
if s[0:2] <= "26":
  dp[1] += 1

for i in range(2, len(s)):
  dp[i] += dp[i-1]
  if s[i-1:i+1] <= "26":
    dp[i] += dp[i-2]


print(dp)
