# from line_profiler import LineProfiler
import json
from typing import List

# Example 1
rectangles = [
    [1, 1, 3, 3],
    [3, 1, 4, 2],
    [3, 2, 4, 4],
    [1, 3, 2, 4],
    [2, 3, 3, 4]
]

# Example 2
# rectangles = [
#     [1, 1, 2, 3],
#     [1, 3, 2, 4],
#     [3, 1, 4, 2],
#     [3, 2, 4, 4]
# ]

# Example 4
# rectangles = [
#     [1, 1, 3, 3],
#     [3, 1, 4, 2],
#     [1, 3, 2, 4],
#     [2, 2, 4, 4]
# ]

# case 1
rectangles = [[1,1,3,3],[3,1,4,2],[3,2,4,4],[1,3,2,4],[2,3,3,4]]

# rectangles = [[0, 0, 4, 1], [7, 0, 8, 2], [6, 2, 8, 3], [5, 1, 6, 3], [4, 0, 5, 1], [
#     6, 0, 7, 2], [4, 2, 5, 3], [2, 1, 4, 3], [0, 1, 2, 2], [0, 2, 2, 3], [4, 1, 5, 2], [5, 0, 6, 1]]


def isRectangleCover(rectangles: List[List[int]]) -> bool:
  z = zip(*rectangles)
  loX = min(z.__next__())
  loY = min(z.__next__())
  hiX = max(z.__next__())
  hiY = max(z.__next__())
  # print(loX, loY, hiX, hiY)
  # if hiX-loX != hiY-loY:
  #   return False

  fields = set([(i, j) for i in range(loX, hiX) for j in range(loY, hiY)])

  for r in rectangles:
    for f in [(i, j) for i in range(r[0], r[2]) for j in range(r[1], r[3])]:
      if f not in fields:
        return False
      fields.remove(f)

  return not fields


# x = isRectangleCover(rectangles)
# print(x)


def cover_segment(rectangles):
  rectangles.sort()

  print(len(rectangles))
  z = zip(*rectangles)
  loX = min(z.__next__())
  loY = min(z.__next__())
  hiX = max(z.__next__())
  hiY = max(z.__next__())
  print(loX, loY, hiX, hiY)

  # x = loX
  takenRects = []
  for x in range(loX, hiX):
    while rectangles and rectangles[0][0] <= x:
      takenRects.append(rectangles.pop(0))

    segs = sorted([(r[1], r[3]) for r in takenRects])
    if not segs or segs[0][0] != loY or segs[-1][1] != hiY:
      return False
    for i in range(1, len(segs)):
      if segs[i-1][1] != segs[i][0]:
        return False

    # del leaving
    takenRects = [r for r in takenRects if r[2] > x+1]

  return True


def cover1(rectangles):
  rectangles.sort()

  print(len(rectangles))
  z = zip(*rectangles)
  loX = min(z.__next__())
  loY = min(z.__next__())
  hiX = max(z.__next__())
  hiY = max(z.__next__())
  print(loX, loY, hiX, hiY)

  # x = loX
  takenRects = []
  col = [False] * (hiY-loY)

  for x in range(loX, hiX):
    currRects = []
    while rectangles and rectangles[0][0] <= x:
      currRects.append(rectangles.pop(0))

    for r in currRects:
      if any(col[r[1]-loY:r[3]-loY]):
        return False
      col[r[1]-loY:r[3]-loY] = [True] * (r[3]-r[1])

    if not all(col):
      return False

    takenRects += currRects

    # mark leaving
    for r in takenRects:
      if r[2] <= x+1:
        col[r[1]-loY:r[3]-loY] = [False] * (r[3]-r[1])

    takenRects = [r for r in takenRects if r[2] > x+1]

  return True


def cover_set(rectangles):
  rectangles.sort()

  print(len(rectangles))
  z = zip(*rectangles)
  loX = min(z.__next__())
  loY = min(z.__next__())
  hiX = max(z.__next__())
  hiY = max(z.__next__())
  print(loX, loY, hiX, hiY)

  # x = loX
  takenRects = []
  # col = [False] * (hiY-loY)
  col = set()
  for x in range(loX, hiX):
    currRects = []
    while rectangles and rectangles[0][0] <= x:
      currRects.append(rectangles.pop(0))

    for r in currRects:
      s = set(range(r[1], r[3]))
      if col.intersection(s):
        return False
      col = col.union(s)

    if len(col) < hiY-loY:
      return False

    takenRects += currRects

    # mark leaving
    for r in takenRects:
      if r[2] <= x+1:
        s = set(range(r[1], r[3]))
        col = col - s

    takenRects = [r for r in takenRects if r[2] > x+1]

  return True




def cover_segment_set(rectangles):
  rectangles.sort()

  print(len(rectangles))
  z = zip(*rectangles)
  loX = min(z.__next__())
  loY = min(z.__next__())
  hiX = max(z.__next__())
  hiY = max(z.__next__())
  print(loX, loY, hiX, hiY)

  takenRects = []
  # col = [False] * (hiY-loY)
  segs = []
  for x in range(loX, hiX):
    currRects = []
    while rectangles and rectangles[0][0] <= x:
      currRects.append(rectangles.pop(0))
    takenRects += currRects

    segs += [(r[1], r[3]) for r in currRects]

    if not segs: #or segs[0][0] != loY or segs[-1][1] != hiY:
      return False
    starts = set([s[0] for s in segs]+[hiY]) 
    stops = set([s[1] for s in segs]+[loY])
    intersections = starts & stops 
    if len(intersections)-1 != len(segs):
      return False

    for i in range(len(takenRects)-1,-1,-1):
      if takenRects[i][2] == x+1:
        segs.remove((takenRects[i][1],takenRects[i][3]))
        del takenRects[i]

    # del leaving
    # takenRects = [r for r in takenRects if r[2] > x+1]

  return True


from bisect import bisect_right
class SegmentCollection:
  def __init__(self):
    self.s = []
  def add(self, el):
    pos = bisect_right(self.s,el)
    if pos > 0 and self.s[pos-1][1] == el[0] and pos < len(self.s) and self.s[pos][0] == el[1]:
      self.s[pos-1][1] = self.s[pos][1]
      del self.s[pos]
    elif pos > 0 and self.s[pos-1][1] == el[0]:
      self.s[pos-1][1] = el[1]
    elif pos < len(self.s) and self.s[pos][0] == el[1]:
      self.s[pos][0] = el[0]
    else:
      self.s.insert(pos,el)
  

def cover_segment_collection(rectangles):
  rectangles.sort()

  print(len(rectangles))
  z = zip(*rectangles)
  loX = min(z.__next__())
  loY = min(z.__next__())
  hiX = max(z.__next__())
  hiY = max(z.__next__())
  print(loX, loY, hiX, hiY)

  takenRects = []
  # col = [False] * (hiY-loY)
  missingSegs = SegmentCollection()
  missingSegs.add([loY,hiY])

  for x in range(loX, hiX):
    currRects = []
    while rectangles and rectangles[0][0] <= x:
      currRects.append(rectangles.pop(0))


    segs = SegmentCollection()
    for r in currRects:
      segs.add([r[1],r[3]])

    if str(segs.s) != str(missingSegs.s):
      return False

    takenRects += currRects
    missingSegs.s = []
    for i in range(len(takenRects)-1,-1,-1):
      if takenRects[i][2] == x+1:
        missingSegs.add([takenRects[i][1],takenRects[i][3]])
        del takenRects[i]

    # del leaving
    # takenRects = [r for r in takenRects if r[2] > x+1]

  return True



# s = SegmentCollection()

# s.add([2,3])
# # s.add([2,3])

# s.add([0,1])
# s.add([3,4])
# s.add([-4,0])
# s.add([1,2])

# print(s.s)

# s2 = SegmentCollection()
# s2.add([-4,4])
# print(s2.s)

# print(str(s.s) == str(s2.s))




with open('testcases/RectangeTest01.txt', 'r') as f:
  rectangles = json.load(f)

print(cover_segment_collection(rectangles))
# x = set(range(-20000, 20000))
# y = set(range(-1000, 20001))
# x = x.union(y)
# # x = x or y
# print(len(x and y))

# curY = loY
# for i,r in enumerate(rectangles):
#   if r[0] <= x and x < r[3]:

# lp = LineProfiler()
# lp_wrapper = lp(cover0)
# lp_wrapper(rectangles)
# lp.print_stats()
