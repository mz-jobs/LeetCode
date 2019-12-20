# import typing
import math
import bisect

# class Solution:
#   def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#     return 0


# nums1 = [1, 3]
# nums2 = [2]

# nums1 = [1, 2]
# nums2 = [3, 4]

nums1 = [1, 2, 5, 7, 12, 13]
nums2 = [4]

N = len(nums1)
M = len(nums2)
L = N+M

# what if  nums1,nums2 empty
# what if index OOB
# i = math.ceil(float(N/2)) - 1
# j = bisect.bisect_left(nums2, nums1[i])

# if i+j == (N+M)/2 (-2?)

i = j = 0

while i+j*2 < N+M-2:
  if i == N:
    j = j+1
  elif j == M:
    i = i+1
  elif nums1[i] < nums2[j]:
    i = i+1
  else:
    j = j+1

print(i, j)
