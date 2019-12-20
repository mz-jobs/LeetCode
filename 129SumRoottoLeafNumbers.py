class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None


t = TreeNode(4)
t.left = TreeNode(9)
t.right = TreeNode(0)
t.left.left = TreeNode(5)
t.left.right = TreeNode(1)


t1 = TreeNode(1)
t1.right = TreeNode(5)


def sumNumbers(self, root: TreeNode) -> int:
  def helper(node, s):
    if not node:
      return s
    if node.left and node.right:
      return helper(node.left, s*10+node.val) + helper(node.right, s*10+node.val)
    if node.left:
      return helper(node.left, s*10+node.val)
    if node.right:
      return helper(node.right, s*10+node.val)
    return s*10+node.val

  return helper(root, 0)


print(sumNumbers(0, t1))
