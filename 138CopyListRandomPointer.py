class Node:
  def __init__(self, val, next, random):
    self.val = val
    self.next = next
    self.random = random


l = Node(1, None, None)
l.next = Node(2, None, None)
l.random = l.next
l.next.random = l.next


def copyRandomList(head: Node) -> Node:
  p = head
  while p:
    n = Node(p.val, p.next, None)
    p.next = n
    p = p.next.next

  p = head
  while p:
    if p.random:
      p.next.random = p.random.next
    p = p.next.next

  new_head = head.next
  p = head
  while p:
    x = p.next
    p.next = p.next.next
    x.next = x.next.next
    p = p.next

  return new_head
