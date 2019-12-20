from typing import List
n = 4


def possiblePositions(queens, row):
  impossiblePositions = set()
  for q in queens:
    impossiblePositions.add(q[1])  # column
    impossiblePositions.add(q[1]+(row-q[0]))  # right-down
    impossiblePositions.add(q[1]-(row-q[0]))  # left-down
  return set(range(n)) - impossiblePositions


solutions = []


def placeQueen(queens, row):
  if row >= n:
    solutions.append(queens)
  for p in possiblePositions(queens, row):
    placeQueen(queens + [(row, p)], row+1)


placeQueen([], 0)
print(solutions)


def getBoard(queens):
  board = [['.']*n for i in range(n)]
  for q in queens:
    board[q[0]][q[1]] = 'Q'
  return [''.join(r) for r in board]


def boardToStr(b):
  return '\n'.join([''.join(r) for r in b])


for s in solutions:
  print('*'*10)
  print(boardToStr(getBoard(s)))
  print('*'*10)


class Solution:
  def solveNQueens(self, n: int) -> List[List[str]]:
    def possiblePositions(queens, row):
      impossiblePositions = set()
      for q in queens:
        impossiblePositions.add(q[1])  # column
        impossiblePositions.add(q[1]+(row-q[0]))  # right-down
        impossiblePositions.add(q[1]-(row-q[0]))  # left-down
      return set(range(n)) - impossiblePositions

    solutions = []

    def placeQueen(queens, row):
      if row >= n:
        solutions.append(queens)
      for p in possiblePositions(queens, row):
        placeQueen(queens + [(row, p)], row+1)

    placeQueen([], 0)

    def getBoard(queens):
      board = [['.']*n for i in range(n)]
      for q in queens:
        board[q[0]][q[1]] = 'Q'
      return [''.join(r) for r in board]

    return [getBoard(s) for s in solutions]
