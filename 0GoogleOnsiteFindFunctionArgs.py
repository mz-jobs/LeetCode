# https://leetcode.com/discuss/interview-question/391709/google-onsite-find-function-arguments


def binSearch(f, target, right):
  left = 1
  while left <= right:
    mid = (left+right)//2
    res = f(mid)
    if res == target:
      return mid
    elif res < target:
      left = mid + 1
    else:
      right = mid - 1
  return -1


x = binSearch(lambda x: x+15, 30, 1000)
print(x)


def findArgs(f, z):
  res = []
  y = 2**32 - 1
  x = 1

  while f(x, 1) <= z:
    found = binSearch(lambda y: f(x, y), z, y)
    if found != -1:
      y = found
      res.append((x, y))
    x += 1
  return res


def f(x, y): return x**2 + y


z = 5

x = findArgs(f, z)
print(x)
