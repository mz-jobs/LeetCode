from typing import List


class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None


preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]
# postorder = [9, 15, 7, 20, 3]


def buildTree_map(inorder: List[int], preorder: List[int]) -> TreeNode:
  d_inorder = {}
  for i, n in enumerate(inorder):
    d_inorder[n] = i

  def h(inorder_left, inorder_right, preorder_left, preorder_right) -> TreeNode:
    if inorder_left == inorder_right:
      return None

    val = preorder[preorder_left]
    pos = d_inorder[val]
    node = TreeNode(val)
    L = pos - inorder_left

    node.left = h(inorder_left, pos, preorder_left+1, preorder_left+1+L)
    node.right = h(pos+1, inorder_right,
                   preorder_left+1+L, preorder_right)
    return node
  return h(0, len(inorder), 0, len(preorder))


t2 = buildTree_map(inorder, preorder)
print(t2.val)
print(t2.left.val)
print(t2.right.val)
print(t2.right.left.val)
print(t2.right.right.val)
