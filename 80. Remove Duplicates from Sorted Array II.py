nums = [1, 1, 1, 2, 2, 3]
# nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]

# Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice and return the new length.
# for i in range(len(nums)-3, -1, -1):
#   if nums[i+2] == nums[i]:
#     del nums[i+2]
# print(nums)

wr = 0
n = -1
n_prev = -1
for rd in range(len(nums)):
  if not (n == nums[rd] and n_prev == nums[rd]):
    n_prev = n
    n = nums[rd]
    nums[wr] = nums[rd]
    wr += 1


print(nums, wr)
