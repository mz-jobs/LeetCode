intervals = [[1, 3], [6, 9]]
newInterval = [2, 5]

# intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
# newInterval = [4, 8]


# 1. Copy begining
ans = []
while intervals and intervals[0][1] < newInterval[0]:
  ans.append(intervals.pop(0))


# 2. Merge middle if overlapping
while intervals and intervals[0][0] <= newInterval[1]:
  newInterval[0] = min(newInterval[0], intervals[0][0])
  newInterval[1] = max(newInterval[1], intervals[0][1])
  intervals.pop(0)

ans.append(newInterval)

# 3. Copy end
while intervals:
  ans.append(intervals.pop(0))


print(intervals)
print(newInterval)
print(ans)
