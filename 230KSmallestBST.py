class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None


t = TreeNode(3)
t.left = TreeNode(1)
t.left.right = TreeNode(2)
t.right = TreeNode(4)


k = 1


def getArray(t):
  if not t:
    return []
  return [t.val] + getArray(t.left) + getArray(t.right)


x = sorted(getArray(t))[k-1]
print(x)


result = []


def helper(t, k):
  if not t or k == 0:
    return k

  k = helper(t.left, k)
  k -= 1
  if k == 0:
    result.append(t.val)
    return 0
  k = helper(t.right, k)
  return k


helper(t, k)
print(result)
