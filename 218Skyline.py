from queue import PriorityQueue

events = PriorityQueue()

buildings = [
    [2, 9, 10],
    [3, 7, 15],
    [3, 12, 12],
    [15, 20, 10],
    [19, 20, 8]]

# buildings = [[1, 2, 1], [1, 2, 2], [1, 2, 3]]
# buildings = [[0, 2, 3], [2, 5, 3]]

for b in buildings:
  events.put((b[0], b[2]))
  events.put((b[1], -b[2]))


res = [list(events.get())]
tops = [0, res[-1][1]]

while not events.empty():
  e = events.get()
  if e[1] >= 0:
    tops.append(e[1])
  else:
    tops.remove(-e[1])

  if not events.empty() and events.queue[0][0] == e[0]:
    continue

  maxTops = max(tops)

  if e[0] == res[-1][0]:
    res[-1][1] = maxTops

  if maxTops != res[-1][1]:
    res.append([e[0], maxTops])

print(res)
