
# https://leetcode.com/problems/container-with-most-water/

import typing


class Solution:
  def maxAreaSimple(self, height: typing.List[int]) -> int:
    max_area = 0
    for i in range(0, len(height)):
      for j in range(i+1, len(height)):
        max_area = max(max_area, min(height[i], height[j]) * (j-i))
    return max_area

  def maxArea(self, height: typing.List[int]) -> int:
    max_area = 0
    i = 0
    j = len(height)-1
    while i < j:
      max_area = max(max_area, min(height[i], height[j]) * (j-i))
      if height[i] < height[j]:
        i = i + 1
      else:
        j = j - 1
    return max_area


print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49)
