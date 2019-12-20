A = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
K = 2

left = right = 0
# whats with left in case K = 0 ?
zeroCount = 0
best = 0

while right < len(A):
  if A[right]:
    right += 1
    if right - left > best:
      best = right - left
  elif zeroCount < K:
    right += 1
    zeroCount += 1
    if right - left > best:
      best = right - left
  else:
    if A[left] == 0:
      zeroCount -= 1
    left += 1
    if zeroCount < 0:
      right = left
      zeroCount = 0


print(best)
