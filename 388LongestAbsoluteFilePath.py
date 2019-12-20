input = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"


best = 0
stack = []
for f in input.split('\n'):
  h = f.count('\t')
  while len(stack) > h:
    del stack[-1]
  stack.append(f[h:])
  if '.' in f:
    s = sum([len(it) for it in stack]) + len(stack)-1
    if s > best:
      best = s
  print(stack)

print(input)

print(best)
