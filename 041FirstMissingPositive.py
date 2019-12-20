from typing import List
t0 = [1, 2, 0]
t1 = [3, 4, -1, 1]
t2 = [7, 8, 9, 11, 12]


def firstMissingPositive(nums: List[int]) -> int:
  return min(set(range(1, len(nums)+2)) - set(nums))


print(firstMissingPositive(t0))
