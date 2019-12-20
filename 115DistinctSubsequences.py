from functools import lru_cache
S = "babgbag"
T = "bag"

# S = "rabbbit"
# T = "rabbit"

# S = ""
# T = "as"


def numDistinct(self, s: str, t: str) -> int:
  @lru_cache(maxsize=None)
  def count(s_i, t_i):
    if t_i >= len(t):
      return 1
    if len(s)-s_i < len(t)-t_i:
      return 0
    if s[s_i] == t[t_i]:
      return count(s_i+1, t_i) + count(s_i+1, t_i+1)
    return count(s_i+1, t_i)
  return count(0, 0)


print(numDistinct(0, S, T))
