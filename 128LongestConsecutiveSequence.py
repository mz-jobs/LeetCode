from functools import lru_cache
from typing import List
nums = [100, 4, 200, 1, 3, 2]


def longestConsecutive(self, nums: List[int]) -> int:
  s = set(nums)
  @lru_cache(maxsize=None)
  def l(x):
    if x not in s:
      return 0
    return l(x+1)+1

  return max([l(n) for n in nums])


print(longestConsecutive(0, nums))
