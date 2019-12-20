from collections import defaultdict
s = "ababbc"
k = 2


def longestSubstring(s: str, k: int):
  for c in set(s):
    if s.count(c) < k:
      return max([longestSubstring(s2, k) for s2 in s.split(c)])
  return len(s)


print(longestSubstring(s, k))

# def longestSubstringLessThanK(s, k):
#   counts = defaultdict(int)
#   if not s or k == 0:
#     return 0

#   i = 0
#   j = 1
#   counts[s[i]] += 1
#   best = 1
#   while j < len(s):
#     if counts[s[j]] < k:
#       counts[s[j]] += 1
#       if j-i+1 > best:
#         best = j-i+1
#       j += 1
#     else:
#       counts[s[i]] -= 1
#       i += 1
#   return best
