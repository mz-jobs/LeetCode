class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None


t1 = TreeNode(-10)
t1.left = TreeNode(9)
t1.right = TreeNode(20)
t1.right.left = TreeNode(15)
t1.right.right = TreeNode(7)


t2 = TreeNode(2)
t2.left = TreeNode(-1)


def maxPathSum(self, root: TreeNode) -> int:

  def helper(node: TreeNode) -> int:
    if not node:
      return 0, -float('inf')
    l, b1 = helper(node.left)
    r, b2 = helper(node.right)
    return max(l, r, 0) + node.val, max(l+r+node.val, max(l, r, 0)+node.val, b1, b2)

  _, best = helper(root)
  return best


print(maxPathSum(0, t1))
print(maxPathSum(0, t2))
