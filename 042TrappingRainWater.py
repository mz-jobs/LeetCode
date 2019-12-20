
import typing


class Solution:
  def trap(self, height: typing.List[int]) -> int:
    N = len(height)
    outline = [0] * N
    outline[0] = height[0]
    # fill left
    for i in range(1, N):
      outline[i] = max(height[i], outline[i-1])

    outline[N-1] = height[N-1]
    # fill right
    for i in range(N-2, -1, -1):
      outline[i] = min(outline[i], max(height[i], outline[i+1]))

    area = 0
    for i in range(N):
      area = area + (outline[i] - height[i])


input = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(Solution().trap(input))
