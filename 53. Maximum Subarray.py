nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# nums = [-2]


def naive(nums):
  best = -float('inf')
  N = len(nums)
  for i in range(N):
    for j in range(i, N):
      s = sum(nums[i:j+1])
      if s > best:
        best = s
  return best


print(naive(nums))


def elegant(nums):
  for i in range(1, len(nums)):
    if nums[i-1] > 0:
      nums[i] += nums[i-1]
  return max(nums)


print(elegant(nums))


# compressed = [nums[0]]
# for n in nums[1:]:
#   if n * compressed[-1] < 0:
#     compressed.append(n)
#   else:
#     compressed[-1] += n

# if compressed[0] < 0:
#   del compressed[0]

# if compressed and compressed[-1] < 0:
#   del compressed[-1]

# for i in range(len(compressed)-3, -1, -2):
#   s = sum(compressed[i:i+3])
#   if s > compressed[i]:
#     compressed[i] = s
#     # del compressed[i+1]
#     # del compressed[i+2]


# print(compressed)
