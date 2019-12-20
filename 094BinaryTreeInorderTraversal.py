arr = [1, None, 2, 3]

# tree creation is a little messed up - Clean


class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None


# t = None

def CreateTree(i, n):
  pos = 2**n-1+i
  if pos >= len(arr) or arr[pos] == None:
    return None
  t = TreeNode(arr[2**n-1+i])
  t.left = CreateTree(i*2, n+1)
  t.right = CreateTree(i*2+1, n+1)
  return t


t = CreateTree(0, 0)

print(t.val)
print(t.left)
print(t.right.val)
print(t.right.left)
print(t.right.right)


# def inorderTraversal(self, root: TreeNode) -> List[int]:
