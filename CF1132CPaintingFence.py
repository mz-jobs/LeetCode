N = 15
intervals = [
    [13, 14],
    [1, 4],
    [4, 5],
    [5, 6],
    [2, 7],
    [10, 10],
]

intervals.sort()

print(intervals)

count = [0] * N
for a, b in intervals:
  print(' '*a + 'x'*(b-a+1))
  for i in range(a, b+1):
    count[i] += 1

print(count)


dp = [[0] * N for _ in range(len(intervals)+1)]

for used in range(1, len(intervals)+1):
  for a, b in intervals:
    for x in range(1, N):
      paintedToX = max(0, min(b, x) - a + 1)
      dp[used][x] = max(dp[used][x], dp[used-1][min(a, x)-1]+paintedToX)

print(' *** DP ***')
for r in dp:
  print(r)

# If sorted You can do it all in one go
dp2 = [0]*N
for a, b in intervals:
  for x in range(1, N):
    paintedToX = max(0, min(b, x) - a + 1)
    dp2[x] = max(dp2[x], dp2[min(a, x)-1]+paintedToX)

print('DP2 ', dp2)
