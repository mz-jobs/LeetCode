n = 4
k = 2


combs = []
nums = list(range(1, n+1))


def addCombination(path, nums):
  if len(path) == k:
    combs.append(path)
    return

  for n in nums.copy():
    nums.remove(n)
    addCombination(path + [n], nums.copy())


addCombination([], nums)
print(combs)
