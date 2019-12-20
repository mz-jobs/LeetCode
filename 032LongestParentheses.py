s = "())((())())"
# s = "()(()"
# s = ")(((((()())()()))()(()))("
# stack = 0
# current = 0
best = 0

level = 0
stack = [[0, 0]]
for c in s:
  if c == ')' and level > 0:
    level -= 1
    if stack[-1][0] == level:
      stack[-1][1] += 2
    else:
      _, el_val = stack.pop()
      stack[-1][1] += 2 + el_val
  elif c == '(':
    level += 1
    stack.append([level, 0])
  else:
    level = 0
    stack.append([0, 0])

for _, el in stack:
  if el > best:
    best = el

# print(best)

print(stack)
print(best)
