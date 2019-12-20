# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example:

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.


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
  def addTwoNumbersWithCarry(self, l1: ListNode, l2: ListNode, carry: int) -> ListNode:
    if l1 == None and l2 == None:
      if carry == 0:
        return None
      else:
        return ListNode(carry)
    if l1 == None:
      l1 = ListNode(0)
    if l2 == None:
      l2 = ListNode(0)
    node = ListNode((l1.val+l2.val+carry) % 10)
    node.next = self.addTwoNumbersWithCarry(
        l1.next, l2.next, (l1.val+l2.val+carry) // 10)
    return node

  def addTwoNumbersList(self, l1: ListNode, l2: ListNode) -> ListNode:
    return self.addTwoNumbersWithCarry(l1, l2, 0)

  def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    head = ListNode(0)
    carry = 0
    current = head
    while l1 or l2 or carry:
      v1 = l1.val if l1 else 0
      v2 = l2.val if l2 else 0
      # node = ListNode((v1+v2+carry) % 10)
      current.next = ListNode((v1+v2+carry) % 10)
      current = current.next
      carry = (v1+v2+carry) // 10
      l1 = l1.next if l1 else None
      l2 = l2.next if l2 else None
    return head.next

  def addTwoNumbers1(self, l1, l2):
    dummy = cur = ListNode(0)
    carry = 0
    while l1 or l2 or carry:
      if l1:
        carry += l1.val
        l1 = l1.next
      if l2:
        carry += l2.val
        l2 = l2.next
      cur.next = ListNode(carry % 10)
      cur = cur.next
      carry //= 10
    return dummy.next

  def addTwoNumbers2(self, l1, l2):
    def toint(node):
      return node.val + 10 * toint(node.next) if node else 0
    n = toint(l1) + toint(l2)
    first = last = ListNode(n % 10)
    while n > 9:
      n = n // 10
      last.next = last = ListNode(n % 10)
    return first


n1 = ListNode(2)
n1.push_back(4)
n1.push_back(3)
n1.print()

n2 = ListNode(5)
n2.push_back(6)
n2.print()

Solution().addTwoNumbers(n1, n2).print()
