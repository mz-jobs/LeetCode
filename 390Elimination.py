

def lastRemaining(n):

  x = list(range(1, n+1))

  left = True

  while len(x) > 1:
    if left:
      x = x[1::2]
    else:
      x = x[len(x) % 2::2]
    left = not left
    # print(x)

  return x[0]


n = 12401

print('Res: ', lastRemaining(n))

step = 1
x = 1
left = True

while(n > 1):
  if left or (not left and n % 2 == 1):
    x += step
  step *= 2
  n //= 2
  left = not left
  print(x, step, n, left)


# for n in range(1, 500):
#   print(n, lastRemaining(n))
