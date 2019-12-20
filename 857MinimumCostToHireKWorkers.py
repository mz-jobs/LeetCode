import heapq

# quality = [3, 1, 10, 10, 1]
# wage = [4, 8, 2, 2, 7]
# K = 3

quality = [10, 20, 5]
wage = [70, 50, 30]
K = 2

# calculate wage/quality for each worker

# calculate proposed wage for every other worker
# select those that will take this wage
# if more or equal than K will take than return by sorted


def minCostToHire0(quality, wage, K):
  h = [(w/q, i) for i, (q, w) in enumerate(zip(quality, wage))]
  heapq.heapify(h)

  print(h)
  minCost = float('inf')
  while h:
    ratio = heapq.heappop(h)
    proposed = [ratio[0]*q for q in quality]
    selected = [p for i, p in enumerate(proposed) if p >= wage[i]]

    print(ratio)
    print('Proposed: ', proposed)
    print('Selected: ', selected)

    if(len(selected) >= K):
      print('Cost: ', sum(sorted(selected)[:K]))
      minCost = min(minCost, sum(sorted(selected)[:K]))
  return minCost


def minCostToHire1(quality, wage, K):
  minCost = float('inf')
  for ratio in [w/q for q, w in zip(quality, wage)]:
    proposed = [ratio*q for q in quality]
    selected = [p for i, p in enumerate(proposed) if p >= wage[i]]

    # print(ratio)
    # print('Proposed: ', proposed)
    # print('Selected: ', selected)

    if(len(selected) >= K):
      cost = sum(heapq.nsmallest(K, selected))
      # print('Cost: ', cost)
      if cost < minCost:
        minCost = cost
  return minCost


def minCostToHire(quality, wage, K):
  cost = float('inf')
  workers = [(w/q, q) for q, w in zip(quality, wage)]
  heap = []  # heap will keep minimal K values
  sumq = 0  # will keep a sum of heap
  for ratio, q in sorted(workers):
    heapq.heappush(heap, -q)
    sumq += q

    if len(heap) > K:
      # will subtract beacuase q was negated in insertion
      sumq += heapq.heappop(heap)

    if len(heap) == K:
      cost = min(cost, sumq*ratio)

  return cost


print('Result: ', minCostToHire(quality, wage, K))
