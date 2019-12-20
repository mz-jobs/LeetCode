m = 5
n = 5
N = 10
i = 0
j = 0


dp = [[0]*(n+2) for _ in range(m+2)]


dp[i+1][j+1] = 1

for step in range(N):
  dp2 = [[0]*(n+2) for _ in range(m+2)]
  for a in range(1, m+1):
    for b in range(1, n+1):
      dp2[a][b-1] += dp[a][b]
      dp2[a][b+1] += dp[a][b]
      dp2[a-1][b] += dp[a][b]
      dp2[a+1][b] += dp[a][b]
  dp = dp2


for r in dp:
  print(r)
