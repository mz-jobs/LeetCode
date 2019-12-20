from functools import lru_cache
from typing import List
grid = [
    [0, 1, -1],
    [1, 0, -1],
    [1, 1,  1]]

grid = [
    [1, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 1]]



grid = [
    [1, 1, -1],
    [1, -1, 1],
    [-1, 1, 1]]

grid = [
  [+0,+0,+1,+0,+0,+1,+0,+1,+1,-1,+0,+0,-1,-1,+0,+1,+1,-1,+0,-1],
  [+1,+1,+1,+0,+1,+0,+0,+0,+0,+1,+1,+1,+1,+1,+1,+1,+0,+0,+1,+0],
  [+1,+0,+1,+1,+0,+0,+1,+0,+0,+0,+1,+0,+1,+1,+1,-1,+0,+1,+1,+0],
  [+0,+1,+1,+0,+0,+0,+1,+0,+1,+1,+0,-1,+1,+0,+0,+1,+0,+0,+1,+1],
  [-1,+0,-1,+1,+0,+0,+1,+1,+0,+0,+1,+1,+0,-1,+1,+0,+0,+0,+1,+1],
  [+0,+0,+1,+0,+1,+1,+0,+0,+1,+0,+0,+1,+0,+1,+1,+1,+1,+1,+1,+0],
  [+0,+0,+0,+1,+0,+1,+1,+0,+0,+1,+1,-1,+1,+0,+1,+1,+0,+1,+1,+0],
  [+0,+0,+0,+0,+0,+0,+1,+0,+0,+1,+0,+0,+1,+0,+0,+0,+1,+0,+1,+1],
  [+0,+0,+0,-1,+1,+0,+0,+1,+0,+0,+1,+1,+1,+1,+0,+0,+0,+1,+1,+0],
  [+1,+0,+1,+1,+1,+0,+0,+1,+1,+0,+1,+0,+0,+0,-1,+0,-1,+0,+1,+0],
  [+0,+1,-1,+1,+1,+1,+1,+0,+1,+0,+0,+1,+1,+0,-1,+1,+0,+0,-1,+0],
  [+0,+0,+0,+0,+1,+0,+1,+0,+0,-1,+0,+1,+0,-1,+0,+0,+1,+0,+1,+1],
  [+1,-1,-1,+0,+0,+1,+1,+1,+0,+1,+1,+1,+1,+1,+1,+0,+0,+0,+1,+0],
  [-1,+0,+1,+1,+1,+1,+1,+1,+0,+1,+1,+1,+1,+1,+0,+0,+1,+0,+1,+0],
  [+0,+1,-1,+1,+1,+1,+0,+0,+1,-1,+1,+1,+0,+1,+0,+1,+0,-1,+1,+0],
  [+1,-1,+1,+0,+1,+1,+1,+0,+0,+0,+1,+1,+1,+1,-1,+0,+0,+1,+0,-1],
  [-1,+1,+0,+0,+0,+1,+1,+1,+1,+1,+0,+1,+1,-1,+0,+1,+0,+0,+1,+0],
  [+0,+0,+0,-1,+0,+1,+0,+0,+0,+0,+0,+0,+1,+0,+1,+1,+0,+0,+0,+1],
  [+0,+1,+0,+0,+0,+0,+0,+0,+0,+1,+1,+1,+1,+0,+0,+1,+0,+0,+0,+1],
  [+0,+0,+0,+1,-1,+0,-1,+1,+0,+1,+0,+0,+0,+0,+1,+0,+0,+1,-1,+0]]

def maxCherries(grid):
  M = len(grid)
  N = len(grid[0])
  # Consider Two people walking at the same time (i1,j1) and (i2,j2)
  # if the step on the same field count in only once
  @lru_cache(maxsize=max(M,N)**3)
  def walk(i1, j1, i2, j2):
    if i1 >= M or i2 >= M or j1 >= N or j2 >= N or grid[i1][j1] == -1 or grid[i2][j2] == -1:
      return -1
    if i1 == i2 and i1 == M-1 and j1 == j2 and j1 == N-1:
      return grid[i1][j1]

    res = max(
        walk(i1+1, j1, i2+1, j2),
        walk(i1+1, j1, i2, j2+1),
        walk(i1, j1+1, i2+1, j2),
        walk(i1, j1+1, i2, j2+1)
    )

    if res == -1:
      return -1

    res += grid[i1][j1] + grid[i2][j2]

    if i1 == i2 and j1 == j2:
      res -= grid[i1][j1]

    return res

  return max(0, walk(0, 0, 0, 0))


def maxCherriesMemo(grid):
  M = len(grid)
  N = len(grid[0])
  # Consider Two people walking at the same time (i1,j1) and (i2,j2)
  # if the step on the same field count in only once
  memo = {}

  def walk(i1, j1, i2, j2):
    if (i1,j1,i2,j2) in memo:
      return memo[(i1,j1,i2,j2)]
    if i1 >= M or i2 >= M or j1 >= N or j2 >= N or grid[i1][j1] == -1 or grid[i2][j2] == -1:
      memo[(i1,j1,i2,j2)] = -1
      return memo[(i1,j1,i2,j2)]
      # return -1
    if i1 == i2 and i1 == M-1 and j1 == j2 and j1 == N-1:
      memo[(i1,j1,i2,j2)] = grid[i1][j1]
      return memo[(i1,j1,i2,j2)]
      # return grid[i1][j1]

    res = max(
        walk(i1+1, j1, i2+1, j2),
        walk(i1+1, j1, i2, j2+1),
        walk(i1, j1+1, i2+1, j2),
        walk(i1, j1+1, i2, j2+1)
    )

    if res == -1:
      memo[(i1,j1,i2,j2)] = -1
      return memo[(i1,j1,i2,j2)]

    res += grid[i1][j1] + grid[i2][j2]

    if i1 == i2 and j1 == j2:
      res -= grid[i1][j1]

    if i1==0 and j1 ==0:
      print('Memo size: ',len(memo))

    memo[(i1,j1,i2,j2)] = res
    return memo[(i1,j1,i2,j2)]
      # return res

  return max(0, walk(0, 0, 0, 0))



print(maxCherries(grid))
print(maxCherriesMemo(grid))

# @lru_cache()
# def maxCherries2(visited, i, j):
#   if i == M-1 and j == N-1:
#     if (i, j) not in visited:
#       res = maxCherries(visited | frozenset([(i, j)]), 0, 0)
#       return grid[i][j] + res[0], res[1]
#     else:
#       return 0, visited

#   if i >= M or j >= N or grid[i][j] == -1:
#     return -1, frozenset()
#   down = maxCherries(visited | frozenset([(i, j)]), i+1, j)
#   right = maxCherries(visited | frozenset([(i, j)]), i, j+1)
#   if down[0] == -1 and right[0] == -1:
#     return -1, frozenset()

#   if down[0] > right[0]:
#     best = down
#   else:
#     best = right

#   if (i, j) in visited:
#     return best
#   else:
#     return best[0] + grid[i][j], best[1] | frozenset([(i, j)])

# res = maxCherries(frozenset(), 0, 0)
# print(res)


def maxPathSum(grid: List[List[int]]) -> int:
  for i in range(1, len(grid)):
    grid[i][0] += grid[i-1][0]

  for j in range(1, len(grid[0])):
    grid[0][j] += grid[0][j-1]

  for i in range(1, len(grid)):
    for j in range(1, len(grid[0])):
      grid[i][j] += max(grid[i-1][j], grid[i][j-1])

  return grid[-1][-1]


print(maxPathSum(grid))
