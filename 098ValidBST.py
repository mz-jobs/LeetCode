# Definition for a binary tree node.
class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None


t = TreeNode(2)
t.left = TreeNode(1)
t.right = TreeNode(3)

t2 = TreeNode(5)
t2.left = TreeNode(1)
t2.right = TreeNode(4)
t2.right.left = TreeNode(3)
t2.right.right = TreeNode(6)


def isValid(n: TreeNode, lbound, rbound) -> bool:
  if not n:
    return True
  if n.val <= lbound or n.val >= rbound:
    return False
  if not isValid(n.left, lbound, n.val):
    return False
  if not isValid(n.right, n.val, rbound):
    return False
  return True


print(isValid(t, -float('inf'), float('inf')))
print(isValid(t2, -float('inf'), float('inf')))
