# Definition for singly-linked list.
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
      print(node.val, end=", ")
      node = node.next
    print(')')


class Solution:
  def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    if (not head):
      return head

    L = 1
    cur = head
    while cur.next:
      L += 1
      cur = cur.next
    if n > L:
      return head
    n = L-n

    if n == 0:
      head = head.next
      return head

    cur = head
    while n > 1:
      cur = cur.next
      n -= 1
    cur.next = cur.next.next

    return head


n = ListNode(1)
n.push_back(2)
n.push_back(3)
n.push_back(4)
n.push_back(5)

s = Solution()
x = s.removeNthFromEnd(n, 0)

x.print()
