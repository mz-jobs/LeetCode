
from typing import List
n = 4
connections = [[0, 1], [1, 2], [2, 0], [1, 3]]


def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
  from collections import defaultdict
  net = defaultdict(set)
  for c in connections:
    net[c[0]].add(c[1])
    net[c[1]].add(c[0])

  def dfs(n):
    if n in visited:
      return
    visited.add(n)
    for c in net[n]:
      dfs(c)

  ans = []
  for c in connections:
    net[c[0]].remove(c[1])
    net[c[1]].remove(c[0])
    visited = set()
    dfs(0)
    if len(visited) != n:
      ans.append(c)
    net[c[0]].add(c[1])
    net[c[1]].add(c[0])

  return ans


print(criticalConnections(0, n, connections))
