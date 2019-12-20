slots1 = [[10, 50], [60, 120], [140, 210]]
slots2 = [[0, 15], [60, 70]]
duration = 8


def intersection(a, b):
  c1 = max(a[0], b[0])
  c2 = min(a[1], b[1])
  return [c1, c2] if c2 > c1 else None


res = []
for a in slots1:
  for b in slots2:
    i = intersection(a, b)
    if i:
      res.append(i)

print(res)


res2 = []
i = 0
j = 0
while i < len(slots1) and j < len(slots2):
  x = intersection(slots1[i], slots2[j])
  if x:
    res2.append(x)

  if slots1[i][1] < slots2[j][1]:
    i += 1
  else:
    j += 1

print(res2)
