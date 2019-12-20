# https://www.youtube.com/watch?v=EuPSibuIKIg

# Given points, find how many rectangles (only perpendicular)

points = set(map(tuple, [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2]]))

ans = []
for x0, y0 in points:
  print(x0, y0)
  up = [(x, y) for x, y in points if x == x0 and y > y0]
  right = [(x, y) for x, y in points if x > x0 and y == y0]

  for x1, y1 in right:
    for x2, y2 in up:
      if (x1, y2) in points:
        ans.append((x0, y0, x1, y2))

print(ans)
