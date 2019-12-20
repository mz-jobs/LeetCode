# https://leetcode.com/discuss/interview-experience/389969/google-l3-seattle-sep-2019-no-offer


class TreeNode:
  def __init__(self, x, parent=None):
    self.val = x
    self.parent = parent
    self.left = None
    self.right = None


t = TreeNode(0)
t.left = TreeNode(1, t)
t.left.left = TreeNode(3, t.left)
t.right = TreeNode(2, t)
t.right.right = TreeNode(4, t.right)


def findRNeighbor(t):
  if not t:
    return None

  def helper(t, lev):
    if not t:
      return None
    if lev == 0:
      return t

    x = helper(t.left, lev-1)
    if x:
      return x

    x = helper(t.right, lev-1)
    if x:
      return x

    return helper(t.parent, lev+1)

  return helper(t.parent, 1)


print(findRNeighbor(t.left.left).val)
