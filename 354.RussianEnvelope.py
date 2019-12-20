from bisect import bisect_left
import json


class Solution(object):
  def maxEnvelopes(self, envelopes):
    """
    :type envelopes: List[List[int]]
    :rtype: int
    """


# envelopes = [[5, 4], [6, 5], [6, 7], [2, 3]]
envelopes = [[1, 2], [2, 3], [3, 4], [3, 5],
             [4, 5], [5, 5], [5, 6], [6, 7], [7, 8]]

with open('testcases/RussianTest01.txt', 'r') as f:
  envelopes = json.load(f)

envelopes = envelopes[:]
print('L: ', len(envelopes))


def maxEnvelopesOn2(envelopes):
  if len(envelopes) == 0:
    return 0
  envelopes.sort()
  dp = [1] * len(envelopes)
  best = 1
  for i in range(len(envelopes)):
    e1 = envelopes[i]
    for j in range(i+1, len(envelopes)):
      e2 = envelopes[j]
      if e2[0] > e1[0] and e2[1] > e1[1]:
        if dp[i]+1 > dp[j]:
          dp[j] = dp[i]+1
          if dp[j] > best:
            best = dp[j]

  # print(envelopes)
  # print(dp)
  print(best)
  return best


print('Result O(n**2): ', maxEnvelopesOn2(envelopes))

# sortedW = sorted(envelopes)
# print(sortedW)


def maxEnvelopes(envelopes):
  envelopes.sort(key=lambda e: [e[0], -e[1]])
  steps = [envelopes[0][1]]
  for e in envelopes[1:]:
    i = bisect_left(steps, e[1])
    if i == len(steps):
      steps.insert(i, e[1])
    else:
      steps[i] = e[1]
  return len(steps)


print('Result O(n*logn): ', maxEnvelopes(envelopes))


# dp = [1] * len(envelopes)
# selected = list(range(len(envelopes)))

# envelopes.sort()
# level = 0
# while selected:
#   # print(selected)
#   newSelected = []
#   for i in range(len(selected)):
#     e1 = envelopes[selected[i]]
#     for j in range(i+1, len(selected)):
#       e2 = envelopes[selected[j]]
#       if e1[0] > e2[0] and e1[1] > e2[1]:
#         newSelected.append(i)
#         break
#   selected = newSelected
#   level += 1

# print(level)

# maxEnvelopes(envelopes)
