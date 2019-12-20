import heapq
from collections import defaultdict
from typing import List
nums = [1, 1, 1, 2, 2, 3]
k = 2


def topKFrequentHeap(self, nums: List[int], k: int) -> List[int]:
  d = defaultdict(int)
  for n in nums:
    d[n] += 1

  h = []
  for n, count in d.items():
    if len(h) < k or count > h[0][0]:
      heapq.heappush(h, (count, n))
    if len(h) > k:
      heapq.heappop(h)

  print([n for _, n in h])


def topKFrequentBucket(self, nums: List[int], k: int) -> List[int]:
  d = defaultdict(int)
  for n in nums:
    d[n] += 1

  bucket = defaultdict(set)
  for n, count in d.items():
    bucket[count].add(n)

  ans = set()
  freq = max(bucket.keys())
  while k > 0:
    ans |= bucket[freq]
    k -= len(bucket[freq])
    freq -= 1

  print(ans)
  print(bucket)


print(topKFrequentBucket(0, nums, k))
