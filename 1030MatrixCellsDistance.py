import heapq

R = 2
C = 3

r0 = 1
c0 = 2


def dist(r, c):
  return abs(r-r0) + abs(c-c0)


h = []
for i in range(R):
  for j in range(C):
    heapq.heappush(h, (dist(i, j), (i, j)))

res = []
while h:
  res.append(heapq.heappop(h)[1])
print(res)


points = [(abs(i-r0)+abs(j-c0), (i, j)) for i in range(R) for j in range(C)]
print([el[1] for el in sorted(points)])
