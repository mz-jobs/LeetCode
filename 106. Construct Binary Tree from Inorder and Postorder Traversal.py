from typing import List


class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None


inorder = [9, 3, 15, 20, 7]
postorder = [9, 15, 7, 20, 3]


def buildTree(inorder: List[int], postorder: List[int]) -> TreeNode:
  if not inorder:
    return None
  val = postorder[-1]
  # pos = d_inorder[val]
  pos = inorder.index(val)
  node = TreeNode(val)

  node.left = buildTree(inorder[:pos], postorder[:pos])
  node.right = buildTree(inorder[pos+1:], postorder[pos:-1])
  return node


def buildTree_map(inorder: List[int], postorder: List[int]) -> TreeNode:
  d_inorder = {}
  for i, n in enumerate(inorder):
    d_inorder[n] = i

  def h(inorder_left, inorder_right, postorder_left, postorder_right) -> TreeNode:
    if inorder_left == inorder_right:
      return None

    val = postorder[postorder_right-1]
    pos = d_inorder[val]
    node = TreeNode(val)
    L = pos - inorder_left

    node.left = h(inorder_left, pos, postorder_left, postorder_left+L)
    node.right = h(pos+1, inorder_right,
                   postorder_left+L, postorder_right-1)
    return node
  return h(0, len(inorder), 0, len(postorder))


t = buildTree(inorder, postorder)

print(t.val)
print(t.left.val)
print(t.right.val)
print(t.right.left.val)
print(t.right.right.val)


t2 = buildTree_map(inorder, postorder)
print(t2.val)
print(t2.left.val)
print(t2.right.val)
print(t2.right.left.val)
print(t2.right.right.val)
