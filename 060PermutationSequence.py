from math import factorial

n = 4
k = 9
k = k-1

numbers = [str(i) for i in range(1, n+1)]


res = []

while numbers:
  fact = factorial(n-1)
  p = k // fact
  k = k % fact
  n = n-1
  res.append(numbers.pop(p))

print(''.join(res))
