from typing import List

image = [[1, 1, 1],
         [1, 1, 0],
         [1, 0, 1]]
sr = 1
sc = 1
newColor = 2


def floodFill(image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
  if not image or not image[0]:
    return []
  M = len(image)
  N = len(image[0])

  old_color = image[sr][sc]
  to_color = [[sr, sc]]

  while to_color:
    x, y = to_color.pop()
    if x < 0 or x >= M or y < 0 or y >= N or image[x][y] != old_color:
      continue
    image[x][y] = newColor
    to_color.append([x+1, y])
    to_color.append([x-1, y])
    to_color.append([x, y+1])
    to_color.append([x, y-1])

  return image


print(floodFill(image, sr, sc, newColor))
