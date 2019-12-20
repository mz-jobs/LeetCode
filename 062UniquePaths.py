# https://leetcode.com/problems/unique-paths/

from scipy.special import binom


m = 7
n = 3
# expected = 28

# n = 7-1
# k = 3
# print(binom(n+k-1, n))


dp = [[0] * m for _ in range(n)]

for i in range(n):
  dp[i][0] = 1

for j in range(m):
  dp[0][j] = 1


for i in range(1, n):
  for j in range(1, m):
    dp[i][j] = dp[i-1][j] + dp[i][j-1]


print(dp)
