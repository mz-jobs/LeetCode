# s = "aasdfxasdfasdfasdfas"
# p = "aasdf.*asdf.*asdf.*asdf.*s"

# s = "aaaaaaaaaaaaab"
# p = "a*a*a*a*a*a*a*a*a*a*a*a*b"

s = "bbabacccbcbbcaaab"
p = "a*b*a*a*c*aa*c*bc*"

# s = 'aa'
# p = 'a*'

# s = "ab"
# p = ".*c"


checked = set()


def isMatch(s_i, p_i):
  if (s_i, p_i) in checked:
    return 0
  checked.add((s_i, p_i))

  if p_i == len(p):
    return s_i == len(s)

  if p_i+1 < len(p) and p[p_i+1] == '*':
    if isMatch(s_i, p_i+2):
      return 1
    elif s_i < len(s) and (s[s_i] == p[p_i] or p[p_i] == '.'):
      if isMatch(s_i+1, p_i):
        return 1
  elif s_i < len(s) and (s[s_i] == p[p_i] or p[p_i] == '.'):
    if isMatch(s_i+1, p_i+1):
      return 1

  return 0


print(isMatch(0, 0))
