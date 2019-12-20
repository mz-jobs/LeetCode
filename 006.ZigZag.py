from itertools import chain
s = "PAYPALISHIRING"
# numRows = 3
numRows = 4


def ZigZag(s, numRows):
  if numRows == 1:
    return s
  step = (numRows-1)*2
  L = len(s)
  out = list(range(0, L, step))

  for row in range(1, numRows-1):
    up = list(range(row, L, step))
    down = list(range(step-row, L, step))
    r = [i for j in zip(up, down) for i in j]
    if len(up) > len(down):
      r += [up[-1]]
    out += r

  out += list(range(numRows-1, L, step))

  return ''.join([s[i] for i in out])


# print(''.join([s[i] for i in r]))

# upRows = [0:4]
# print()
# print(s)
# print(''.join([str(i % 10) for i in range(0, L)]))
# print()


def ZigZag2(s, numRows):
  if numRows == 1:
    return s
  step = (numRows-1)*2
  L = len(s)

  upRows = []
  downRows = []
  for i in range(0, L, step):
    upRows.append(range(i+1, i+numRows-1))
    downRows.append(range(i+step-1, i+numRows-1, -1))

  res = list(range(0, L, step))
  res += list(chain(*zip(*chain(*zip(upRows, downRows)))))
  res += list(range(numRows-1, L, step))

  # print(upRows)
  # print(downRows)
  # flat = list(chain(*zip(upRows, downRows)))
  # res += list(chain(*zip(*flat)))
  # print(flat)
  # print(res)
  return ''.join([s[i] for i in res if i < L])


print(ZigZag(s, numRows))
print(ZigZag2(s, numRows))
# print('PAHNAPLSIIGYIR ---- 3')
print('PINALSIGYAHRPI ---- 4')
