

mat = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]


def rotateL(mat):
  if len(mat) == 0:
    return []
  return [[r[-i] for r in mat] for i in range(1, len(mat[0])+1)]


n = 3

# m1 = [list(r) for r in zip(*mat[::-1])]
# print(m1)


def rotateR(mat):
  if len(mat) == 0:
    return []
  return [list(r) for r in zip(*mat[::-1])]
  # return [[r[i] for r in mat[::-1]] for i in range(0, len(mat[0]))]


last = n*n
M = [[last]]
while last > 1:
  M = [list(range(last-len(M), last))] + rotateR(M)
  last = last - len(M[0])


print(M)


# ******************************************************************************


# class Solution:
#     def generateMatrix(self, n: int) -> List[List[int]]:
#         def rotateR(mat):
#           if len(mat) == 0:
#             return []
#           return [[r[i] for r in mat[::-1]] for i in range(0, len(mat[0]))]


#         numbers = list(range(n*n, 0, -1))
#         M = [[numbers.pop(0)]]

#         while numbers:
#           l = len(M[0])
#           M.append(numbers[:l])
#           numbers = numbers[l:]
#           M = rotateR(M)

#         M = rotateR(M)
#         return M
# ******************************************************************************

# def rotateL(mat):
#   if len(mat) == 0:
#     return []
#   return [[r[-i] for r in mat] for i in range(1, len(mat[0])+1)]


# solution = []
# while len(mat) > 0:
#   solution += mat.pop(0)
#   mat = rotate(mat)

# print(solution)


# def spiral(m, n):
#   x = 0  # row
#   y = 0  # column

#   yield(x, y)
#   count = 1

#   up = False
#   while count < m*n:

#     if (x < m/2) and (y < n-x-1) and not up:  # go right
#       y += 1

#     elif (y >= n//2) and (x < m-(n-y)):  # go down
#       x += 1

#     elif (x >= m/2) and (y >= 0+(m-x)):  # go left
#       y -= 1

#     elif (y < n//2) and (x > y+1):  # go up
#       x -= 1
#       up = True
#     else:
#       up = False
#       continue

#     yield (x, y)
#     count += 1


# for i in list(spiral(2, 10)):
#   print(i)


# print([mat[x][y] for x, y in list(spiral(3, 4))])
