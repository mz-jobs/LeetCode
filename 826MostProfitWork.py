from bisect import bisect_right
from collections import OrderedDict


# from itertools import tp
difficulty = [2, 4, 8, 6, 10, 10, 10]
profit = [10, 45, 40, 30, 50, 100, 1]
worker = [4, 5, 6, 7]


difficulty.append(0)
profit.append(0)
jobs = sorted(zip(difficulty, profit))
bestJobs = [jobs[0]]
for j in jobs:
  if j[1] > bestJobs[-1][1]:
    if j[0] == bestJobs[-1][0]:
      bestJobs[-1] = j
    else:
      bestJobs.append(j)


# print(jobs)
# print(bestJobs)

total = 0
for w in worker:
  i = bisect_right(bestJobs, (w, 10001))
  total += bestJobs[i-1][1]
print(total)

# keys=list(jobs.keys())
# for i in range(1, len(keys)):
#   print(keys[i-1], keys[i])
#   if jobs[keys[i-1]] > jobs[keys[i]]:
#     # You can delete item as well, but not while iterating
#     # new list needed?
#     jobs[keys[i]]=jobs[keys[i-1]]

# total=0
# for w in worker:
#   i=bisect_right(keys, w)
#   print(jobs[keys[i-1]])
#   total += jobs[keys[i-1]]


# for ability in worker:
# pay = bisect_right(, ability)
# profit += pay

# print(profit)

# def getPay(ability):
#   if ability not in payList:
# r = bisect_right([j[0] for j in jobs], ability)
#     pay = max([j[1] for j in jobs[:r]]+[0])
#     payList[ability] = pay
#   return payList[ability]


# profit = [getPay(w) for w in worker]
# print(profit, sum(profit))


# v1
# profit = 0
# for w in worker:
#   available = [j[1] for j in jobs if j[0] <= w]
#   profit += max(available)
# print(profit)
