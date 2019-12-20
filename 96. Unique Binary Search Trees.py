# Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

# Example:

# Input: 3
# Output: 5
# Explanation:
# Given n = 3, there are a total of 5 unique BST's:

#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3

import functools


@functools.lru_cache(maxsize=None)
def numTrees(n: int) -> int:
  if n <= 1:
    return 1

  total = 0
  for root in range(n):
    total += numTrees(root) * numTrees(n-root-1)
  return total


print(numTrees(1))
print(numTrees(2))
print(numTrees(3))
