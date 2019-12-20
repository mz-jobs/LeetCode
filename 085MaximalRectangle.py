# matrix = [
#     ["1", "0", "1", "0", "0"],
#     ["1", "0", "1", "1", "1"],
#     ["1", "1", "1", "1", "1"],
#     ["1", "0", "0", "1", "0"]
# ]
from bisect import bisect_left, bisect_right
matrix = [
    ["0", "0", "1", "1"],
    ["0", "1", "1", "1"],
    ["1", "1", "1", "1"],
    ["1", "1", "1", "1"]
]  # last should have [2,4], [3,3],[4,2]


# RULES:
# Add same and larger numbers to the front
# ex. [6,5,5,2,1]
# means: 1x6, 3x5, 4x2, 5x1 beacause 6 contains 5, 5 contains 2, etc.
# Add lower number in place and change all before, because it blocks out all higher
# ex. adding 3 would make [3,3,3,3,2,1], because 3 takes over 6,5,5 , also increases 2,1


# STEPS will need to flip the array
class Steps:

  def __init__(self, steps):
    self.steps = steps

  def add(self, x):
    p = bisect_right(self.steps, x)
    while p < len(self.steps):
      self.steps[p] = x
      p += 1

    self.steps.append(x)

  def __repr__(self):
    return f's{self.steps}'

  def area(self):
    return max([(i+1)*e for i, e in enumerate(self.steps[::-1])])


# s = Steps([1])
# s.add(4)
# s.add(5)
# s.add(5)
# print('s', s.steps)
# s.add(3)
# print('s', s.steps)

# exp = 6

for i in range(len(matrix)):
  for j in range(len(matrix[0])):
    if matrix[i][j] == '1':
      if j > 0 and matrix[i][j-1]:
        matrix[i][j] = matrix[i][j-1]+1
      else:
        matrix[i][j] = 1
    else:
      matrix[i][j] = 0
print(matrix)


stepMat = [[None]*len(matrix[0]) for _ in range(len(matrix))]
for j in range(len(matrix[0])):
  stepMat[0][j] = Steps([matrix[0][j]])

for i in range(1, len(matrix)):
  for j in range(len(matrix[0])):
    stepMat[i][j] = Steps(stepMat[i-1][j].steps.copy())
    stepMat[i][j].add(matrix[i][j])


print(stepMat)

print(max([s.area() for row in stepMat for s in row]))
