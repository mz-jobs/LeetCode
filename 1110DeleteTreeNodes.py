root = [1, 2, 3, 4, 5, 6, 7]


class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None


# t = None

def CreateTree(i, n):
  if 2**n-1+i >= len(root):
    return None
  t = TreeNode(root[2**n-1+i])
  t.left = CreateTree(i*2, n+1)
  t.right = CreateTree(i*2+1, n+1)
  return t


t = CreateTree(0, 0)


def treeHeight(t):
  if not t:
    return 0
  return 1 + max(treeHeight(t.left), treeHeight(t.right))


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


# printTree(t)


# def delVal(t, to_del):
#   if t and t.left.val in to_del:
#     t.left = None


processList = [t]


def pruneTree(t, to_delete):
  if not t:
    return None
  if t.val in to_delete:
    processList.append(t.left)
    processList.append(t.right)
    return None
  t.left = pruneTree(t.left, to_delete)
  t.right = pruneTree(t.right, to_delete)
  return t


results = []
while processList:
  results.append(pruneTree(processList.pop(0), [3, 5]))

for t in results:
  print('TREE', treeToArray(t))
