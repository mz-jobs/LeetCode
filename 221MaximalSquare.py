matrix = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"],
          ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]


M = len(matrix)
N = len(matrix[0])


grid = [[1 if matrix[i][j] == '1' else 0
         for j in range(N)] for i in range(M)]

for i in range(1, M):
  for j in range(1, N):
    if matrix[i][j] == '1':
      grid[i][j] = 1 + min(grid[i-1][j-1], grid[i-1][j], grid[i][j-1])


print(grid)
m = max(max(grid))
print(m*m)
