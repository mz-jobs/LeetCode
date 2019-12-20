sweetness = [1, 2, 3, 4, 5, 6, 7, 8, 9]
K = 5

sweetness = [5, 6, 7, 8, 9, 1, 2, 3, 4]
K = 8

sweetness = [1, 2, 2, 1, 2, 2, 1, 2, 2]
K = 2


low = min(sweetness)
high = sum(sweetness)//K


while low != high:

  proposition = (low + high+1)//2
  used = 0
  s = 0
  for p in sweetness:
    s += p
    if s >= proposition:
      s = 0
      used += 1

  print(proposition, used)
  if used > K:
    low = proposition
  else:
    high = proposition-1


print(low)
