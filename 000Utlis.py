
# TREE


class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

  def height(self, t):
    if not t:
      return 0
    return 1 + max(self.height(t.left), self.height(t.right))


class Tree:
  def __init__(self, array):

    def CreateTree(i, n):
      if 2**n-1+i >= len(array):
        return None
      t = TreeNode(array[2**n-1+i])
      t.left = CreateTree(i*2, n+1)
      t.right = CreateTree(i*2+1, n+1)
      return t

    self.base = CreateTree(0, 0)


print('H:   ', treeHeight(t))


def treeToArray(tree):
  H = treeHeight(t)
  array = [None] * (2**H - 1)

  def fillArray(i, n, tree):
    if tree:
      array[2**n-1+i] = tree.val
      fillArray(i*2, n+1, tree.left)
      fillArray(i*2+1, n+1, tree.right)

  fillArray(0, 0, tree)
  while array and array[-1] == None:
    array.pop()
  return array


print('A:   ', treeToArray(t))


def printTree(t):
  if t:
    print(t.val)
    printTree(t.left)
    printTree(t.right)
  else:
    print(None)
