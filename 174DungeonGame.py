from typing import List
dungeon = [
    [-2, -3, 3],
    [-5, -10, 1],
    [10, 30, -5]
]


def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
  if not dungeon or not dungeon[0]:
    return 1

  M = len(dungeon)
  N = len(dungeon[0])

  dp = [[float('inf')] * N for _ in range(M)]
  dp[-1][-1] = 1 + max(0, -dungeon[-1][-1])

  for i in range(M-2, -1, -1):
    hpNeeded = dp[i+1][-1] - dungeon[i][-1]
    dp[i][-1] = max(1, hpNeeded)

  for j in range(N-2, -1, -1):
    hpNeeded = dp[-1][j+1] - dungeon[-1][j]
    dp[-1][j] = max(1, hpNeeded)

  for i in range(M-2, -1, -1):
    for j in range(N-2, -1, -1):
      hpNeeded = min(dp[i][j+1], dp[i+1][j]) - dungeon[i][j]
      dp[i][j] = max(1, hpNeeded)

  # for r in dp:
  #   print(r)

  return dp[0][0]


print(calculateMinimumHP(0, [[-5]]))
