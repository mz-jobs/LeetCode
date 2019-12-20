import heapq
from typing import List


class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None


def printList(l):
  arr = []
  while l:
    arr.append(l.val)
    l = l.next
  print(arr)


l1 = ListNode(1)
l1.next = ListNode(4)
l1.next.next = ListNode(5)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

l3 = ListNode(2)
l3.next = ListNode(6)


def mergeKLists(self, lists: List[ListNode]) -> ListNode:
  h = []
  for l in lists:
    if l:
      heapq.heappush(h, (l.val, id(l), l))
  print(h)

  head = ListNode(0)
  curr = head
  while h:
    _, _, l = heapq.heappop(h)
    curr.next = l
    curr = curr.next
    if l.next:
      heapq.heappush(h, (l.next.val, id(l.next), l.next))

  return head.next


L = [l1, l2, l3]
for l in L:
  printList(l)

x = mergeKLists(0, L)
printList(x)
