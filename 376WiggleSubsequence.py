
nums = [1, 7, 4, 9, 2, 5]
nums = [30, 1, 17, 5, 10, 13, 15, 10, 5, 16, 8]


def wiggleUp(nums):
  seq = [-float('inf')]

  for n in nums:
    if len(seq) % 2 == 1:  # next should be higher
      if n > seq[-1]:
        seq.append(n)
      else:
        seq[-1] = n
    else:  # next should be lower
      if n < seq[-1]:
        seq.append(n)
      else:
        seq[-1] = n

  if seq[0] == -float('inf'):
    del seq[0]

  print(seq)
  return len(seq)


u = wiggleUp(nums)
d = wiggleUp([-n for n in nums])
print(u, d)


up = 1
down = 1

for i in range(1, len(nums)):
  if nums[i] > nums[i-1]:
    up, down = down+1, down
  if nums[i] < nums[i-1]:
    up, down = up, up+1

print(up, down)

s = set(range(10**9))
