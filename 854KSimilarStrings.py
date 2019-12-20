import collections
from functools import lru_cache
A = "aabc"
B = "abca"

# Consider couches and graph !!


# A = list(A)
# B = list(B)


@lru_cache(maxsize=None)
def KSimilarStringsRecurrent(A, B):
  if not A and not B:
    return 0
  if A[0] == B[0]:
    return KSimilarStringsRecurrent(A[1:], B[1:])

  res = []
  for i, c in enumerate(B):
    if c == A[0]:
      res.append(1 + KSimilarStringsRecurrent(A[1:], B[1:i]+B[0]+B[i+1:]))
  return min(res)


print(KSimilarStringsRecurrent(A, B))

search = []
d = collections.defaultdict(list)
for i, c in enumerate(B):
  if A[i] != c:
    d[c].append(i)
    search.append(i)

print(search, d)

# swaps = 0
# while search:
# find cycle, for now disregard multiple
x = search.pop(0)

cycle_nodes = [x, d[A[x]][0]]
while cycle_nodes[-1] != cycle_nodes[0]:
  cycle_nodes.append(d[A[cycle_nodes[-1]]][0])

print(cycle_nodes)
