from functools import lru_cache
s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"

s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbbaccc"


@lru_cache(maxsize=None)
def helper(s1: str, s2: str, s3: str) -> bool:
  if (not s1 and s2 == s3) or (not s2 and s1 == s3):
    return True
  if not s1 or not s2:
    return False
  if s1[0] == s3[0] and helper(s1[1:], s2, s3[1:]):
    return True
  if s2[0] == s3[0] and helper(s1, s2[1:], s3[1:]):
    return True
  return False


print(helper(s1, s2, s3))
