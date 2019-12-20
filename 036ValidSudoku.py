from typing import List

def row(b,i): 
  return b[i]

def col(b,i):
  return [r[i] for r in b]

def square(b,i):
  x = i%3*3
  y = i//3*3
  return [r[x:x+3] for r in b[y:y+3]]

def squareL(b,i):
  return [x  for r in square(b,i) for x in r]

def isValid(s):
  s = ''.join(s).replace('.','')
  return len(set(s)) == len(s)

class Solution:
  def isValidSudoku(self, board: List[List[str]]) -> bool:
    rowCheck = [isValid(row(board, i)) for i in range(9)]
    colCheck = [isValid(col(board, i)) for i in range(9)]
    squareCheck = [isValid(squareL(board, i)) for i in range(9)]
    return all(rowCheck+colCheck+squareCheck)

# Very clever solution
  def isValidSudoku2(self, board: List[List[str]]) -> bool:
      ret = []
      for i, row in enumerate(board):
          for j,digit in enumerate(row):
              if digit != '.':
                  ret+=[(digit,i),(j,digit),(i // 3, j // 3, digit)]
      return len(ret) == len(set(ret))


def isValidSudoku(board: List[List[str]]) -> bool:
  pass


b = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
print(b[0])



print('row', row(b,5))
print('col', col(b,3))
print('sq', square(b,8))


rowCheck = [isValid(row(b, i)) for i in range(9)]
colCheck = [isValid(col(b, i)) for i in range(9)]
squareCheck = [isValid(squareL(b, i)) for i in range(9)]
a = rowCheck + colCheck + squareCheck

print(all(a))

