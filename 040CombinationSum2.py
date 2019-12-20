candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8

candidates.sort()
print(candidates)


solutions = set()


def walker(path, pathSum, i):
  if i >= len(candidates):
    return
  if pathSum + candidates[i] == target:
    solutions.add(tuple(path + [candidates[i]]))
    return
  elif pathSum + candidates[i] > target:
    return
  else:
    walker(path + [candidates[i]], pathSum + candidates[i], i+1)
    walker(path, pathSum, i+1)
  return


walker([], 0, 0)
print(solutions)
