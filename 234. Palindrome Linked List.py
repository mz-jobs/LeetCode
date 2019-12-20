class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None


l1 = ListNode(1)
l1.next = ListNode(2)

l2 = ListNode(1)
l2.next = ListNode(2)
l2.next.next = ListNode(2)
l2.next.next.next = ListNode(1)


def isPalindrome(head: ListNode) -> bool:
  def listLen(head: ListNode) -> int:
    n = 0
    while head:
      n += 1
      head = head.next
    return n

  def reverse_list(head: ListNode) -> ListNode:
    rev_list = None
    while head:
      nxt = head.next
      head.next = rev_list
      rev_list = head
      head = nxt
    return rev_list

  def compare_lists(h1, h2):
    while h1 and h2 and h1.val == h2.val:
      h1 = h1.next
      h2 = h2.next
    return h1 == None and h2 == None

  L = listLen(head)
  if L <= 1:
    return True

  x = head
  for _ in range(L//2-1):
    x = x.next
  h2 = x.next
  x.next = None

  if L % 2 == 1:
    h2 = h2.next
  h2 = reverse_list(h2)
  return compare_lists(head, h2)


print(isPalindrome(l1))
