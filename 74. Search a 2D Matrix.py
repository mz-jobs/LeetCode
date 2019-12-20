from bisect import bisect_left
matrix = [
    [1,   3,  5,  7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
]


target = 49


def searchMatrix(matrix, target):
  for row in matrix:
    if row[0] > target:
      break
    x = bisect_left(row, target)
    if x < len(row) and row[x] == target:
      return True
  return False


print(searchMatrix(matrix, target))
