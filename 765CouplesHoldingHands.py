import random
row = [0, 2, 1, 3]
row = [3, 2, 0, 1]

random.seed(1)

row = random.sample(range(10), 10)

print(row)
pos = dict(zip(row, range(len(row))))


swaps = 0
for i in range(0, len(row), 2):
  a = row[i]
  b = a+1 if a % 2 == 0 else a-1
  if pos[b] != i+1:
    x = row[i+1]
    row[i+1] = b
    row[pos[b]] = x
    pos[x] = pos[b]
    pos[b] = i+1

    swaps += 1


print(row)
print(swaps)
