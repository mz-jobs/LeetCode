class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None


def stringToTreeNode(input):
  input = input.strip()
  input = input[1:-1]
  if not input:
    return None

  inputValues = [s.strip() for s in input.split(',')]
  root = TreeNode(int(inputValues[0]))
  nodeQueue = [root]
  front = 0
  index = 1
  while index < len(inputValues):
    node = nodeQueue[front]
    front = front + 1

    item = inputValues[index]
    index = index + 1
    if item != "null":
      leftNumber = int(item)
      node.left = TreeNode(leftNumber)
      nodeQueue.append(node.left)

    if index >= len(inputValues):
      break

    item = inputValues[index]
    index = index + 1
    if item != "null":
      rightNumber = int(item)
      node.right = TreeNode(rightNumber)
      nodeQueue.append(node.right)
  return root


def treeNodeToString(root):
  if not root:
    return "[]"
  output = ""
  queue = [root]
  current = 0
  while current != len(queue):
    node = queue[current]
    current = current + 1

    if not node:
      output += "null, "
      continue

    output += str(node.val) + ", "
    queue.append(node.left)
    queue.append(node.right)
  return "[" + output[:-2] + "]"


# t = stringToTreeNode("[1,3,null,null,2]")
# root = stringToTreeNode("[3,1,4,null,null,2]")
root = stringToTreeNode("[3,null,2,null,1]")
# t = stringToTreeNode("[2,3,1]")
print(treeNodeToString(root))


# def search_fix(lbound, rbound, node):
#   if not node:
#     return None

#   misfitL = search_fix(lbound, min(rbound, node.val), node.left)
#   if misfitL and (misfitL.val < lbound or misfitL.val > rbound):
#     return misfitL

#   misfitR = search_fix(max(lbound, node.val), rbound, node.right)
#   if misfitR and (misfitR.val < lbound or misfitR.val > rbound):
#     return misfitR

#   if node.val < lbound or node.val > rbound:
#     return node

#   if misfitL and misfitR:
#     misfitL.val, misfitR.val = misfitR.val, misfitL.val
#   elif misfitL and not misfitR:
#     misfitL.val, node.val = node.val, misfitL.val
#   elif not misfitL and misfitR:
#     misfitR.val, node.val = node.val, misfitR.val

#   return None


# search_fix(-float('inf'), float('inf'), root)


def fix(root):
  el1 = None
  el2 = None
  prevElement = TreeNode(-float('inf'))

  def traverse(node):
    nonlocal el1
    nonlocal el2
    nonlocal prevElement

    if not node:
      return

    traverse(node.left)

    if not el1 and prevElement.val >= node.val:
      el1 = prevElement

    if el1 and prevElement.val > node.val:
      el2 = node

    prevElement = node

    traverse(node.right)

  traverse(root)
  el1.val, el2.val = el2.val, el1.val


fix(root)

print(treeNodeToString(root))
