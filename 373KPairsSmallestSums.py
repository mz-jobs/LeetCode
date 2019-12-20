# https://leetcode.com/problems/find-k-pairs-with-smallest-sums/


# nums1 = [1, 7, 11]
# nums2 = [2, 4, 6]
# k = 3

import heapq

nums1 = [1, 1, 2]
nums2 = [1, 2, 3]
k = 14

out = []
for n1 in nums1:
  for n2 in nums2:
    out.append((n1+n2, n1, n2))

out.sort()
print([(it[1], it[2]) for it in out])


def kSmallestPairs(nums1, nums2, k):
  if (not nums1) or (not nums2):
    return []

  result = []
  h = [(nums1[0]+nums2[0], 0, 0)]

  while k > 0 and h:
    _, i, j = heapq.heappop(h)
    result.append((nums1[i], nums2[j]))
    # result.append((nums1[i], nums2[j],s))
    k -= 1
    if j == 0 and i+1 < len(nums1):
      heapq.heappush(h, (nums1[i+1]+nums2[j], i+1, j))
    if j+1 < len(nums2):
      heapq.heappush(h, (nums1[i]+nums2[j+1], i, j+1))
  print(result)
  return result


kSmallestPairs(nums1, nums2, k)
