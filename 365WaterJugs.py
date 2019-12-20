class Solution(object):
  def canMeasureWater(self, x, y, z):
    """
    :type x: int
    :type y: int
    :type z: int
    :rtype: bool
    """
    from fractions import gcd
    z % gdc(x, y)


x = 17
y = 11


checked = set()
states = [(0, 0)]

possible = set()


def addState(s):
  if s[0] >= 0 and s[0] <= x and s[1] >= 0 and s[1] <= y and s not in checked:
    states.append(s)


while states:
  s = states.pop(0)
  possible.add(s[0]+s[1])
  checked.add(s)
  # empty
  addState((0, s[1]))
  addState((s[0], 0))
  # fill
  addState((s[0], y))
  addState((x, s[1]))

  # pour 0->1 until empty and until full
  addState((0, s[0]+s[1]))
  addState((s[0]-(y-s[1]), y))
  # pour 1->0 until empty and until full
  addState((s[0]+s[1], 0))
  addState((x, s[1]-(x-s[0])))


print(possible)
# print(checked)


x = 0


def printX():
  y = x+1
  print(y)


printX()
x = 3
printX()
