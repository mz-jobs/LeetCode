# https://leetcode.com/problems/unique-paths-iii/


grid = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]]


m = len(obstacleGrid)
n = len(obstacleGrid[0])


dp = [0] * n

for i in range(n):
  if obstacleGrid[0][i]:
    break
  dp[i] = 1

for j in range(1, m):
  print(dp)
  if obstacleGrid[j][0]:
    dp[0] = 0
  for i in range(1, n):
    if obstacleGrid[j][i]:
      dp[i] = 0
    else:
      dp[i] += dp[i-1]


print(dp)
