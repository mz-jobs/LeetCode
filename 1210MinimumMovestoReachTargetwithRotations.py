from typing import List
grid = [[0, 0, 0, 0, 0, 1],
        [1, 1, 0, 0, 1, 0],
        [0, 0, 0, 0, 1, 1],
        [0, 0, 1, 0, 1, 0],
        [0, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 0, 0]]


def minimumMoves(self, grid: List[List[int]]) -> int:
  if not grid or not grid[0]:
    return -1
  N = len(grid)
  finish = [N-1, N-2, N-1, N-1]
  states = set([(0, 0, 0, 1)])
  visited = states.copy()

  i = 0
  while states:
    new_states = set()
    for r1, c1, r2, c2 in states:
      if [r1, c1, r2, c2] == finish:
        return i
      if r1 == r2:  # horizont
        if c2+1 < N and grid[r2][c2+1] == 0:
          new_states.add((r1, c1+1, r2, c2+1))
        if r1+1 < N and grid[r1+1][c1] == 0 and grid[r2+1][c2] == 0:
          new_states.add((r1+1, c1, r2+1, c2))
          # if not rot:
          new_states.add((r1, c1, r1+1, c1))

      if c1 == c2:  # vertical
        if r2+1 < N and grid[r2+1][c2] == 0:
          new_states.add((r1+1, c1, r2+1, c2))
        if c1+1 < N and grid[r1][c1+1] == 0 and grid[r2][c2+1] == 0:
          new_states.add((r1, c1+1, r2, c2+1))
          # if not rot:
          new_states.add((r1, c1, r1, c1+1))

    states = new_states - visited
    visited |= new_states

    i += 1
    # print(new_states)
  return -1


print(minimumMoves(0, grid))
