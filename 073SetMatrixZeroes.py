
from typing import List
matrix = [
    [0, 1, 2, 0],
    [3, 4, 5, 2],
    [1, 3, 1, 5]
]


def setZeroes(matrix: List[List[int]]) -> None:
  if not matrix or not matrix[0]:
    return

  rows = set()
  cols = set()

  for i in range(len(matrix)):
    for j in range(len(matrix[i])):
      if matrix[i][j] == 0:
        rows.add(i)
        cols.add(j)

  for i in rows:
    for j in range(len(matrix[i])):
      matrix[i][j] = 0

  for i in range(len(matrix)):
    for j in cols:
      matrix[i][j] = 0

  return


setZeroes(matrix)
print(matrix)
