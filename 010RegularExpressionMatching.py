# Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).

# Note:

# s could be empty and contains only lowercase letters a-z.
# p could be empty and contains only lowercase letters a-z, and characters like . or *.

# TODO test for a*a
# TODO test aaa in  a*c*a


def isMatch(s: str, p: str) -> bool:
  x = [pos for pos, char in enumerate(p) if char == '*']
  for i in range(len(x)):
    x[i] -= 1+i
  p = p.replace('*', '')

  # fix for a*a --> move *
  for i in range(len(x)):
    while x[i]+1 < len(p) and p[x[i]] == p[x[i]+1]:
      x[i] += 1

  # print(p)
  # print(''.join(['*' if i in x else ' ' for i in range(len(p))]))

  s_i = 0
  p_i = 0
  last = '!'
  while s_i < len(s) and p_i < len(p):
    if (s[s_i] == p[p_i]) or (p[p_i] == '.'):
      s_i += 1
      if not p_i in x:
        last = '!'
        p_i += 1
      else:
        last = s[s_i-1]
    elif p_i in x:
      p_i += 1
    else:
      break

  while p_i < len(p) and (p_i in x or p[p_i] == last):
    p_i += 1

  # print(s_i)
  # print(p_i)

  print(s_i == len(s) and p_i == len(p))
  return s_i == len(s) and p_i == len(p)


# Example 1:
# Input:
s = "aa"
p = "a"
isMatch(s, p)

# Output: false
# Explanation: "a" does not match the entire string "aa".
# Example 2:

# Input:
s = "aa"
p = "a*"
isMatch(s, p)

# Output: true
# Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
# Example 3:

# Input:
s = "ab"
p = ".*"
isMatch(s, p)

# Output: true
# Explanation: ".*" means "zero or more (*) of any character (.)".
# Example 4:

# Input:
s = "aab"
p = "c*a*b"
isMatch(s, p)

# Output: true
# Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".
# Example 5:

# Input:
s = "mississippi"
p = "mis*is*p*."
isMatch(s, p)
# Output: false

s = "aaa"
p = "ab*a*c*a"
isMatch(s, p)
