from collections import Counter
from functools import lru_cache
from collections import defaultdict
# s1 = "xabcdex"
# s2 = 'xcaedbx'

# s1 = "abcdefghijklmn"
# s2 = "efghijklmndacb"

s1 = 'great'
s2 = 'rgeat'

s1 = 'abcd'
s2 = 'cabd'


def matchScramble(s1, s2):
  if s1 == s2:
    return True

  if len(s1) != len(s2) or Counter(s1) != Counter(s2):
    return False

  d = defaultdict(int)
  for c in s1:
    d[c] += 1
  for c in s2:
    d[c] -= 1

  if any(d.values()):
    return False

  for p in range(1, len(s1)):
    # print('P ', p)
    # print('Straight')
    # print(s1[:p], s1[p:])
    # print(s2[:p], s2[p:])
    # print('Cross')
    # print(s1[:p], s1[p:])
    # print(s2[:len(s2)-p], s2[-p:])

    if matchScramble(s1[:p], s2[:p]) and matchScramble(s1[p:], s2[p:]):
      return True
    if matchScramble(s1[:p], s2[-p:]) and matchScramble(s1[p:], s2[:len(s2)-p]):
      return True

  return False


print(matchScramble(s1, s2))
# print(Counter(s1) == Counter(s2))

# test s1 and s2 starting with 'a'

# WRONG for
# 'abcd'
# 'cabd'
# def matchScramble2(s1, s2):
#   if s1 == s2:
#     return True
#   if Counter(s1) != Counter(s2):
#     return False

#   # Fix s1 try to split s2 at every point
#   c = s1[0]
#   for p in [p for p, letter in enumerate(s2) if letter == c]:
#     print('P: ', p, '*'*20)
#     print('Cross')
#     print(s1[:len(s2)-p], s1[len(s2)-p:])
#     print(s2[:p], s2[p:])
#     print('Straight')
#     print(s1[:p+1], s1[p+1:])
#     print(s2[:p+1], s2[p+1:])

#     if p == 0:
#       if matchScramble(s1[1:], s2[1:]):
#         return True
#     elif p == len(s2)-1:
#       if matchScramble(s1[1:], s2[:-1]):
#         return True
#     elif matchScramble(s2[p:], s1[:len(s2)-p]) and matchScramble(s2[:p], s1[len(s2)-p:]):
#       return True
#     elif matchScramble(s1[:p+1], s2[:p+1]) and matchScramble(s1[p+1:], s2[p+1:]):
#       return True
#   return False


# print(matchScramble(s1, s2))
# d = dict()
# for c in s1:
#   d[c] = set(c)

# def getScrambles(s):
#   if s in d:
#     return d[s]

#   d[s] = set()
#   for div in range(1, len(s)):
#     left_set = getScrambles(s[:div])
#     right_set = getScrambles(s[div:])
#     for x1 in left_set:
#       for x2 in right_set:
#         d[s].add(x1+x2)
#         d[s].add(x2+x1)
#   return d[s]

# x = getScrambles(s1)
# print(sorted(list(x)))

# print(s2 in x)
