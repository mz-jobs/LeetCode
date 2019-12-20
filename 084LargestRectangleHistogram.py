heights = [2, 1, 2]

stack = []
best = 0

heights.append(0)

for i in range(len(heights)):
  x = i
  while stack and heights[i] < stack[-1][1]:
    x, h = stack.pop()
    area = (i-x)*h
    if area > best:
      best = area
  stack.append([x, heights[i]])

print(best)


def largestRectangleArea(height):
  height.append(0)
  stack = [-1]
  ans = 0
  for i in range(len(height)):
    while height[i] < height[stack[-1]]:
      h = height[stack.pop()]
      w = i - stack[-1] - 1
      ans = max(ans, h * w)
    stack.append(i)
  height.pop()
  return ans


print(largestRectangleArea(heights))
