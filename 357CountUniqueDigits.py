

# for i in range(0,100):
count = 0
for n in range(0, 10**6):
  if len(set([int(s) for s in str(n)])) == len(str(n)):
    count += 1
print(count)

n = 6

for n in range(0, 11):

  total = 0
  for i in range(10-n+1, 10):
    total = total*i + i
  total *= 9
  total += 10
  print(n, 'Total: ', total)

ans = [
    1,
    10,
    91,
    739,
    5275,
    32491,
    168571,
    712891,
    2345851,
    5611771,
    8877691]

print(ans[6])
