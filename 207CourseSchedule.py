from collections import defaultdict
from functools import lru_cache
from typing import List
# numCourses = 2
# prerequisites = [[1, 0]]

numCourses = 3
prerequisites = [[0, 1], [0, 2], [1, 2]]


# IDEA negate -> coursesNotDone
# IDEA use only prerequisites to track courses not done

def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
  d = defaultdict(set)
  for c, p in prerequisites:
    d[c].add(p)

  @lru_cache(maxsize=numCourses)
  def dfs(c):
    if c in visitedNow:
      return False
    visitedNow.add(c)
    if c in d.keys():
      for pre in d[c]:
        if not dfs(pre):
          return False
    return True

  for c in d.keys():
    visitedNow = set()
    if not dfs(c):
      return False
  return True


print(canFinish(numCourses, prerequisites))


def canFinish2(numCourses: int, prerequisites: List[List[int]]) -> bool:
  coursesDone = set(range(numCourses))
  d = defaultdict(set)
  for c, p in prerequisites:
    d[c].add(p)
    coursesDone.discard(c)

  grow = True
  while grow:
    grow = False
    for c in set(range(numCourses))-coursesDone:
      if d[c].issubset(coursesDone):
        coursesDone.add(c)
        grow = True

  return len(coursesDone) == numCourses
