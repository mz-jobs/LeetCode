# Priorities:
# 1. Min Total Cost
# 2. Min different sellers (ie. max # of 0 in plan)
# 3. More bread earlier

import heapq


def calculate_purchasing_plan(total_days, sellers):
  # Approach:
  # Find min cost by storing in heap, complexity should be O(N*log N), where N=len(sellers)
  # by default buy early, this will satisfy priority 3
  # if buying with new seller, check if all bread from old seller can be bough at new = least transations (priority 2)
  DAYS_FRESH = 30
  INITIAL_BREAD = 10
  # Note: for clarity we process initial bread at the end, but it also can be checked early

  # if sellers were pre-sorted we could simplify, but for now
  # Force event at day==total_days / also so we don't nead to check if sellers is empty
  sellers.append((total_days, 0))
  sellers.append((0, float('inf')))  # Consider necessary initial bread
  sellers = [(p, d, i) for i, (d, p) in enumerate(sellers)]
  sellers.sort(key=lambda x: (x[1], x[0], x[2]))

  sellers_bak = sellers.copy()  # needed for initial bread at the end

  plan = [[] for _ in range(len(sellers))]  # store the plan through intervals
  h = []
  d = 0
  prev = None
  while d < total_days:
    while d >= sellers[0][1]:
      # Optionally remove older, more expensive bread
      while h and h[0][0] > sellers[0][0]:
        heapq.heappop(h)
      heapq.heappush(h, sellers.pop(0))
    while h and d >= h[0][1]+DAYS_FRESH:  # remove stale bread
      heapq.heappop(h)

    if not h:
      return None

    # if whole prev can be trasfered to new, do it as it will minimize # of transactions
    if prev and prev != h[0] and prev[0] == h[0][0] and plan[prev[2]][0][0] >= h[0][1] and plan[prev[2]][-1][1] < h[0][1]+DAYS_FRESH:
      plan[h[0][2]] = plan[prev[2]]
      plan[prev[2]] = []

    next_d = min(sellers[0][1], h[0][1]+DAYS_FRESH)
    plan[h[0][2]].append((d, next_d))
    prev = h[0]
    d = next_d

  plan_total = [x[-1][1] - x[0][0] if x else 0 for x in plan]

  # INITIAL BREAD:
  # By default if bought bread at vendor 2, he has cheper bread than 1
  # It should then be enough to remove staring from left
  free_bread = INITIAL_BREAD - plan_total[-1]
  if free_bread < 0:
    return None
  i = 0
  while free_bread > 0 and sellers_bak[i][1] < DAYS_FRESH:
    x = min(free_bread, plan_total[sellers_bak[i][2]])
    plan_total[sellers_bak[i][2]] -= x
    free_bread -= x
    i += 1

  return plan_total[0:-2]


tests = []


tests.append(([10, []],
              [], 'Self sustained'))

tests.append(([10, [(5, 20)]],
              [0], 'Self sustained 2'))

tests.append(([11, []],
              None, 'Forced to eat stale'))

tests.append(([35, [(11, 20)]],
              None, 'Forced to eat stale 2'))

tests.append(([60, [(10, 200), (15, 100), (35, 500), (50, 30)]],
              [5, 30, 5, 10], 'example in problem description'))

tests.append(([55, [(10, 50), (15, 100), (20, 100), (25, 150), (35, 100)]],
              [30, 0, 0, 0, 15], 'minimize # of sellers used'))

tests.append(([55, [(10, 100), (25, 100)]],
              [30, 15], 'more bread earlier'))

tests.append(([55, [(10, 50), (15, 100), (20, 100), (45, 50)]],
              [30, 5, 0, 10], 'minimize # of sellers used and buy earlier'))

tests.append(([55, [(10, 50), (15, 100), (20, 100), (25, 100), (48, 50)]],
              [30, 0, 8, 0, 7], 'hard case, seller at t=15 wont last, seller at t=25 will not satisfy buy earlier'))

tests.append(([55, [(10, 50), (15, 100), (20, 100), (25, 100), (48, 150)]],
              [30, 0, 0, 15, 0], 'same as above, but this time S at t=25 can last till end'))

tests.append(([30, [(1, 100), (4, 90), (11, 80), (12, 50)]],
              [0, 1, 1, 18], 'Using initial bread'))

tests.append(([55, [(10, 50), (20, 90), (25, 100)]],
              [30, 10, 5], 'Merging test'))

tests.append(([55, [(0, 50), (20, 90), (25, 100)]],
              [20, 20, 5], 'Initial bread 2'))

tests.append(([55, [(20, 90), (25, 100), (0, 50)]],
              [20, 5, 20], 'Initial bread 3'))


for case, solution, explanation in tests:
  print('Case: ', case)
  print('Result:  ', calculate_purchasing_plan(*case))
  print('Solution:', solution, ' - ', explanation, '\n')
