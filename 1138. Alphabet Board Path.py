target = "leet"
target = "code"


def pos(x):
  return ((ord(x)-ord('a')) % 5, (ord(x)-ord('a'))//5)


def dist(x1, x2):
  return x2[0]-x1[0], x2[1]-x1[1]


path = []
start = 'a'
for c in target:
  h, v = dist(pos(start), pos(c))
  # print(h, v)
  if h >= 0:
    if v >= 0:
      path.append('D'*v + 'R'*h)
    else:
      path.append('U'*(-v) + 'R'*h)
  else:
    if v >= 0:
      path.append('L'*(-h) + 'D'*v)
    else:
      path.append('L'*(-h) + 'U'*(-v))

  start = c

path.append('')

print('!'.join(path))
