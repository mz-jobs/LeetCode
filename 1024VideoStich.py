from typing import List
clips = [[0, 2], [4, 6], [8, 10], [1, 9], [1, 5], [5, 9]]
T = 10


def videoStitching(clips: List[List[int]], T: int):
  clips.sort()

  count = 0
  position = 0
  while position < T:
    selected = []
    while clips and position >= clips[0][0]:
      selected.append(clips.pop(0)[1])
    # print(selected)
    # print(clips)
    if not selected:
      return -1
    position = max(selected)
    count += 1

  return count


print(videoStitching(clips, T))
