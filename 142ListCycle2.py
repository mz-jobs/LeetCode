class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

  def push_front(self, x):
    node = ListNode(x)
    node.next = self
    self = node
    return self

  def push_back(self, x):
    if self.next == None:
      self.next = ListNode(x)
    else:
      self.next.push_back(x)

  def print(self):
    print('(', end="")
    node = self
    while node:
      print(node.val, end="->")
      node = node.next
    print(')')


L = ListNode(1)
L.push_back(2)
L.push_back(3)
L.push_back(4)
L.push_back(5)
L.push_back(6)


L.print()

head = L
n = head
visited = {}
visited[id(n)] = 0
i = 1
while n.next:
  x = id(n.next)
  if x in visited:
    return visited[x]

  visited[x] = i
  i += 1
return -1
