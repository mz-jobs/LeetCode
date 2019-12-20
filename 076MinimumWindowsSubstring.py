from collections import defaultdict, Counter
S = "ADOBECODEBANC"
T = "ABC"

# S = 'aaa'
# T = 'aa'


def minWindowSet(self, s: str, t: str) -> str:
  if not s or not t:
    return ''

  T = set(t)
  available = set()
  count = defaultdict(int)

  best = len(s)+1
  ans = ''

  i = 0
  j = 0
  while i < len(s):
    if T.issubset(available):
      if j-i < best:
        best = j-i
        ans = s[i:j]
      if s[i] in count:
        count[s[i]] -= 1
        if count[s[i]] == 0:
          available.remove(s[i])
      i += 1
    elif j < len(s):
      if s[j] in T:
        available.add(s[j])
        count[s[j]] += 1
      j += 1
    else:
      break

  return ans


def minWindow(self, s: str, t: str) -> str:
  if not s or not t:
    return ''

  cnt = Counter(t)
  best = len(s)+1
  ans = ''

  i = j = 0
  while i < len(s):
    if not list(cnt.elements()):  # returns non-zero
      if j-i < best:
        best = j-i
        ans = s[i:j]
      if s[i] in cnt:
        cnt[s[i]] += 1
      i += 1
    elif j < len(s):
      if s[j] in cnt:
        cnt[s[j]] -= 1
      j += 1
    else:
      break

  return ans


print(minWindow(0, S, T))
print(minWindow(0, S, ''))
# count[S[j]]
