# Definition for singly-linked list.
class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None


def array_to_list(array):
  l = None
  for x in array[::-1]:
    n = ListNode(x)
    n.next = l
    l = n
  return(n)


def list_to_array(l):
  a = []
  while l:
    a.append(l.val)
    l = l.next
  return a


l1 = array_to_list([1, 4, 3, 2, 5, 2])
print(list_to_array(l1))


def partition(self, head: ListNode, x: int) -> ListNode:
  if not head or not head.next:
    return head

  res = ListNode(-1)
  res.next = head

  greater = ListNode(-1)  # guard
  greater_it = greater
  cur = res
  while cur.next:
    if cur.next.val < x:
      cur = cur.next
    else:
      greater_it.next = cur.next
      cur.next = cur.next.next
      greater_it.next.next = None
      greater_it = greater_it.next

  cur.next = greater.next
  return res.next


print(list_to_array(partition(0, l1, 3)))
