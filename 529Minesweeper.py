board = [['E', 'E', 'E', 'E', 'E'],
         ['E', 'E', 'M', 'E', 'E'],
         ['E', 'E', 'E', 'E', 'E'],
         ['E', 'E', 'E', 'E', 'E']]


# def addDigit(x, y):
#   if x < 0 or x > len(board[0]) or y < 0 or y > len(board):
#     return
#   if board[y][x] == 'E':
#     board[y][x] = '1'
#   elif board[y][x] in '012345678':
#     board[y][x] = str(int(board[y][x]) + 1)


# for y, row in enumerate(board):
#   for x, item in enumerate(row):
#     if board[y][x] == 'M':
#       for j in range(y-1, y+2):
#         for i in range(x-1, x+2):
#           addDigit(i, j)


def countMines(x, y):
  fragment = [it for row in board[max(y-1, 0):min(y+2, len(board))]
              for it in row[max(x-1, 0):min(x+2, len(board[0]))]]
  # print('y ', max(y-1, 0), min(y+2, len(board)))
  # print('x ', max(x-1, 0), min(x+2, len(board[0])))
  return fragment.count('M')

  # return   == 'M'])


def click(x, y):
  if x < 0 or x >= len(board[0]) or y < 0 or y >= len(board) or board[y][x] == 'B':
    return
  if board[y][x] == 'M':
    board[y][x] = 'X'
    return
  mines = countMines(x, y)
  if mines != 0:
    board[y][x] = str(mines)
  else:
    board[y][x] = 'B'
    for j in range(y-1, y+2):
      for i in range(x-1, x+2):
        click(i, j)


click(0, 0)
for r in board:
  print(r)

# for y, row in enumerate(board):
#   for x, item in enumerate(row):
#     print(x, y, ':', countMines(x, y))
