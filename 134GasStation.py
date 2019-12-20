from typing import List
dummy = ''
# gas = [1, 2, 3, 4, 5]
# cost = [3, 4, 5, 1, 2]
gas = [1, 2, 3, 4, 5, 5, 70]
cost = [2, 3, 4, 3, 9, 6, 2]


def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
  N = len(gas)
  netto = [g-c for g, c in zip(gas, cost)]
  for i in range(N):
    total = 0
    for j in range(N):
      total += netto[(i+j) % N]
      if total < 0:
        break
    if total >= 0:
      return i
  return -1


def canCompleteCircuitBetter(self, gas: List[int], cost: List[int]) -> int:
  n = len(gas)

  if n < 1:
    return -1
  if sum(gas) - sum(cost) < 0:
    return -1

  curr = 0
  start = 0

  for i in range(n):
    curr += gas[i] - cost[i]

    if curr < 0:
      start = i+1
      curr = 0

  return start


print(canCompleteCircuit(dummy, gas, cost))
# for r in dp:
#   print(r)
# print('Solution ', solution)

# def costToTravel(i, j):
#   # returns gasLeft, minGasInTank
#   if i == j:
#     return 0, 0
#   # if i >= N or j >= N:
#   #   return costToTravel(i % N, j % N)
#   res = costToTravel(i+1, j)
#   g = gas[i % N] - cost[i % N]

#   return g + res[0], g-res[0]

# for i in range(N):
#   print(costToTravel(i, i-1+N))
