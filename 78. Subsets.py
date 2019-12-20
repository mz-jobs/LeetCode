nums = [1, 2, 3]


results = []


def create(path, start_i):
  results.append(path.copy())
  for i in range(start_i, len(nums)):
    create(path+[nums[i]], i+1)
  return


create([], 0)

print(results)
