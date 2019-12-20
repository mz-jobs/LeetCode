# def movesToStamp(self, stamp: str, target: str) -> List[int]:


from typing import List
stamp = "abca"
target = "abababcabcaabcaaaaaaaaaca"


stamp = "qr"
target = "qrqqqrqrqrrqrqr"


stamp = "aq"
target = "aqaaqaqqqaqqaaq"

stamp = "zbs"
target = "zbzbsbszbssbzbszbsss"

# x = target.find(stamp)
# solution.append(x)


def movesToStamp(self, stamp: str, target: str) -> List[int]:

  # def reduceL(base, stamp, pos=0):
  #   x = len(base)
  #   solution = []
  #   while x:  # Try adding a largest stamp possible on
  #     i = min(x, len(stamp))
  #     # print(target[x-i:x], stamp[:i])
  #     while base[x-i:x] != stamp[:i]:
  #       i -= 1
  #     if i == 0:
  #       return []
  #     x -= i
  #     solution.append(x+pos)
  #   return solution

  # def reduceR(base, stamp, pos=0):
  #   return [pos + len(base) - x-len(stamp) for x in reduceL(base[::-1], stamp[::-1])]

  # def reduceM(base, stamp, pos=0):
  #   solution = reduceL(base, stamp)
  #   if solution:
  #     base = base[:solution[-1]]

  def reduceM(base, stamp, pos=0, allowLeft=True, allowRight=True):
    solution = []
    # -1 because after split full len is not possible
    i = min(len(base), len(stamp)-1)
    while base and i > 0:
      if allowLeft and base[:i] == stamp[-i:]:
        solution.append(pos + i-len(stamp))
        base = base[i:]
        pos += i
        i = min(len(base), len(stamp))
      elif allowRight and base[-i:] == stamp[:i]:
        solution.append(pos+len(base)-i)
        base = base[:-i]
        i = min(len(base), len(stamp))
      else:
        i -= 1
    if base and i == 0:
      x = stamp.find(base)
      if allowLeft and allowRight and x != -1:
        solution.append(pos-x)
        return solution
      return []
    return solution

  solution = []
  pieces = target.split(stamp)
  pos = [0]
  for x in pieces[:-1]:
    solution.append(pos[-1]+len(x))
    pos.append(pos[-1]+len(x)+len(stamp))

  if pieces[0]:
    x = reduceM(pieces[0], stamp, allowLeft=False)
    if not x:
      return []
    solution.extend(x)

  if pieces[-1]:
    x = reduceM(pieces[-1], stamp, pos[-1], allowRight=False)
    if not x:
      return []
    solution.extend(x)

  for s, p in zip(pieces[1:-1], pos[1:-1]):
    if s:
      x = reduceM(s, stamp, p)
      if not x:
        return []
      solution.extend(x)

  return solution[::-1]


solution = movesToStamp(0, stamp, target)

test = list(' '*len(target))
for x in solution:
  print(' '*(x) + stamp)
  test[x:x+len(stamp)] = list(stamp)


print(''.join(test))
print(target)

# print(reduceM('bca', stamp, 0))
