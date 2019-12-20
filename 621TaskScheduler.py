
from collections import deque
from collections import Counter
from queue import PriorityQueue
from typing import List
import heapq

tasks = ["A", "A", "A", "B", "B", "B", "C", "D", "E", "E"]
n = 2


def leastIntervalCounter(self, tasks: List[str], n: int) -> int:

  count = Counter(tasks)
  last_used = dict(zip(count.keys(), [-n-1]*len(count.keys())))

  print(last_used)
  print(count-1)

  t = 0
  while count:
    available = [task for task, _ in count.most_common()
                 if last_used[task]+n+1 <= t]
    if available:
      count[available[0]] -= 1
      count = +count
      last_used[available[0]] = t
    t += 1

  print(t)
  return t


def leastIntervalHeap(self, tasks: List[str], n: int) -> int:
  count = Counter(tasks)
  h = [(-c, task) for task, c in count.items()]
  heapq.heapify(h)
  q = deque()  # for resting

  t = 0
  while h or q:
    if q and q[0][0] <= t:
      heapq.heappush(h, q.popleft()[1])
    if h:
      c, task = heapq.heappop(h)
      if -c > 1:
        q.append((t+n+1, (c+1, task)))
    t += 1

  return t


def leastInterval(self, tasks: List[str], n: int) -> int:
  # if not tasks:
    # return 0
  count = Counter(tasks)
  t = 0
  cycle = []
  while count:
    cycle = count.most_common(n+1)
    for k, _ in cycle:
      count[k] -= 1
    count = +count
    t += n+1
  t -= n+1 - len(cycle)
  return t


print(leastInterval(0, tasks, n))
leastInterval(0, [], n)
print(leastIntervalHeap(0, tasks, n))
