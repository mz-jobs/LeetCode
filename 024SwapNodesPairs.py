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


def swap2(n1, n2):
  n1.next = n2.next
  n2.next = n1
  return n2


if not head:
  return head
if not head.next:
  return head

cur = head
head = swap2(cur, cur.next)
while cur.next and cur.next.next:
  cur.next = swap2(cur.next, cur.next.next)
  cur = cur.next.next

head.print()


# tmp = cur.next
# cur.next = cur.next.next
# tmp.next = cur
# L = tmp

# L.print()
# print(L)
