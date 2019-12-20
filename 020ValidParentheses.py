from collections import deque
s = "()[]{}"


def validParentheses(s):
  stack = deque()
  for c in s:
    if c in '([{':
      stack.append(c)
    elif stack:
      p = stack.pop()
      if p+c not in ['()', '[]', '{}']:
        return False
    else:
      return False
  return len(stack) == 0


x = validParentheses(s)
print(x)
