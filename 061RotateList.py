# Definition for singly-linked list.
class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

# class Solution:


def printList(h):
  while h:
    print(f'{h.val}->', end='')
    h = h.next
  print('NULL')


h = ListNode(1)
h.next = ListNode(2)
h.next.next = ListNode(3)
h.next.next.next = ListNode(4)
h.next.next.next.next = ListNode(5)

printList(h)


def rotateRight(head: ListNode, k: int) -> ListNode:

  if (not head) or (not head.next) or (k == 0):
    return head

  n = 1
  fwd = h
  while fwd.next:
    n += 1
    fwd = fwd.next
  fwd.next = h

  k = n - (k % n)
  fwd = head
  for _ in range(k-1):
    fwd = fwd.next
  head = fwd.next
  fwd.next = None
  return head


x = rotateRight(h, 3)
printList(x)
