import copy
candidates = [2, 3, 6, 7, 13]
target = 7

# solutions = {}
# for c in candidates:
#   solutions[c] = [[c]]


solutions = []
proposition = [0]*len(candidates)
proposition[0] = 1


def increaseProp():
  # find first non zero
  i = 0
  while proposition[i] == 0:
    i += 1

  if i >= len(proposition)-1:
    return True

  proposition[i+1] += 1
  proposition[i] = 0
  return False


while True:
  s = sum([x[0]*x[1] for x in zip(proposition, candidates)])
  if s == target:
    solutions.append(proposition.copy())
  if s > target:
    if increaseProp():
      break
  else:
    proposition[0] += 1

# [[candidates[it[0]]] * it[1] for s in solutions for it in enumerate(s)]
print(solutions)

s = solutions[1]
print(s)


# print([getSolution(s) for s in solutions])
# for i in range(target):
#   for c in candidates:
#     if i in solutions:
#       for s in solutions:
#         if s+c in solutions:
#           solutions[s+c].append

# def solve(state, state_sum):
#   # print('Solving ', state)
#   if state_sum > target:
#     return
#   if state_sum == target:
#     print(state)
#     return
#   for c in candidates:
#     solve(state + [c], state_sum + c)
#   return

# def update_dict(d, pos, item):
#   if pos not in d:
#     d[pos] = []
#   d[pos].append(item)


# solutions = {0: set()}
# for c in candidates:
#   starts = list(solutions.keys())
#   for k in starts:
#     for i in range(1, (target-k)//c + 1):
#       if k+c*i not in solutions:
#         solutions[k+c*i] = set()
#         # solutions[k+c*i] = solutions[k].copy()
#       if k+c*i == 20:
#         print(k, c, i)
#       solutions[k+c*i].add(k+c*(i-1))
#       # for j in range(len(solutions[k+c*i])):
#       #   solutions[k+c*i][j].append([c]*i)
#       # # solutions[k+c*i].append([c]*i)

# print(solutions[4])
# print(solutions[6])
# print(solutions[7])

# print(solutions[20])


# d = {}
# d[1] = [1, 2, 3, 4]
# d[2] = d[1].copy()

# d[2].append(0)

# print(d)
# def getS(i):
#   print(i)
#   if i <= 0:
#     return []
#   return [[i-item] + getS(i-item) for item in solutions[i]]


# print(getS(7))


# solutions = {0:[]}
# for c in candidates:
#   starts = list(solutions.keys())
#   for k in starts:
#     for i in range(1, (target-k)//c + 1):
#       if k+c*i not in solutions:
#         solutions[k+c*i] = []
#       sols = [sol+[c]*i for sol in solutions[k]]
#       # print(sols)
#       solutions[k+c*i].append(sols)


# print(solutions)
