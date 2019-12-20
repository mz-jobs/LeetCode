# https://leetcode.com/discuss/interview-question/397339/google-oa-2020-min-cost-to-keep-employees


from collections import defaultdict
hiring = 1
salary = 4
severance = 12

employees = [3, 5, 1, 3, 6, 2, 4]


# v1
# DP O(N*K*K) K = max(N)

# dp = [defaultdict(lambda: float('inf')) for _ in range(len(employees))]
dp = [dict() for _ in range(len(employees))]
dp[0][employees[0]] = employees[0]*(hiring+salary)
for i in range(1, len(employees)):
  for e in dp[i-1]:
    if e <= employees[i]:  # hire maybe
      cost = dp[i-1][e] + e * salary + (employees[i]-e)*(hiring+salary)
      if employees[i] not in dp[i] or cost < dp[i][employees[i]]:
        dp[i][employees[i]] = cost
    else:  # fire
      for to_fire in range(e - employees[i]+1):
        cost = dp[i-1][e] + (e-to_fire)*salary + to_fire*severance
        if e-to_fire not in dp[i] or cost < dp[i][e-to_fire]:
          dp[i][e-to_fire] = cost

print(dp)


# v2
# keep minimum employees, fire employees into stack, re-hire if needed

hiring = 1
salary = 4
severance = 12
employees = [3, 5, 1, 3, 6, 2, 4]

e = 0
cost = 0
fired = []
for i in range(len(employees)):
  while e < employees[i]:
    e += 1
    if fired and (i-fired[-1])*salary < severance + hiring:
      cost += (i-fired[-1])*salary
      fired.pop()
    else:
      cost += hiring  # just hire

  while e > employees[i]:
    e -= 1
    fired.append(i)

  cost += e * salary

while fired and (i-fired[-1]+1)*salary < severance:
  cost += (i-fired[-1]+1)*salary
  fired.pop()

print('Total', cost+len(fired)*severance)
