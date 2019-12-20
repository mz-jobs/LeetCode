import random

random.seed(1)


class SkiplistNode:
  def __init__(self, x, next=None, prev=None, top=None, down=None):
    self.val = x

    self.next = next
    if next:
      next.prev = self

    self.prev = prev
    if prev:
      prev.next = self

    self.down = down
    if down:
      down.top = self

    self.top = top
    if top:
      top.down = self

  def toArray(self):
    array = []
    p = self
    while p:
      array.append(p.val)
      p = p.next
    return array

  def remove(self):
    self.prev.next = self.next
    if self.next:
      self.next.prev = self.prev
    if self.top:
      self.top.remove()
    del self

  # def findAtLevel(x):
  #   p = self
  #   while p.val < x and p.next:
  #     p = p.next
  #   return p

  # def find(x):
  #   p = self.findAtLevel(x)
  #   if p.val = x:


class Skiplist:
  def __init__(self):
    self.promote_chance = 0.5
    self.head = SkiplistNode(-1)
    SkiplistNode(-1, top=self.head)

  def findNode(self, target: int) -> SkiplistNode:
    p = self.head
    while True:
      while p.next and p.next.val <= target:
        p = p.next
      if p.down:
        p = p.down
      else:
        break
    return p

  def getUpper(self, node):
    p = node.prev
    while not p.top:
      p = p.prev
    return p.top

  def search(self, target: int) -> bool:
    x = self.findNode(target)
    return x.val == target

  def add(self, num: int) -> None:
    p = self.findNode(num)
    n = SkiplistNode(num, p.next, p)
    # Ensure You're promoting the topleft node
    while n.prev.val == num:
      n = n.prev
    while n.top:
      n = n.top
    # Try promoting
    while random.random() < self.promote_chance:
      x = self.getUpper(n)
      n = SkiplistNode(num, prev=x, next=x.next, down=n)
      if x == self.head:  # EXTEND ONE LEVEL
        self.head = SkiplistNode(-1, down=x)
        break

  def erase(self, num: int) -> bool:
    n = self.findNode(num)
    if n.val != num:
      return False
    if n.next and n.next.val == num:  # can delete on right
      n = n.next

    n.remove()
    return True

  def toArray(self):
    array = []
    p = self.head
    while p:
      array.append(p.toArray())
      p = p.down
    return array


l = Skiplist()

# for i in range(15):
# l.add(i)
# l.add(3)
# l.add(7)
# l.add(5)
# l.add(2)
# x = 'add'
# arg = 4

# print(l.toArray())
# print(l.erase(5))
# print(l.erase(7))
# print(l.toArray())


input1 = ["add","add","add","add","add","add","add","add","add","add","add","search","search","erase","erase","add","search","erase","search","search","add","search","add","erase","erase","add","erase","erase","erase","search","search","erase","erase","erase","search","add","add","add","add","erase","erase","add","add","erase","erase","erase","search","search","add","add","erase","erase","search","add","search","search","search","search","search","search","search","search","search","search","search","search"]
input2 = [[3],[14],[3],[18],[1],[18],[17],[8],[5],[16],[3],[10],[9],[14],[13],[18],[11],[16],[1],[4],[7],[0],[5],[12],[11],[20],[17],[2],[1],[4],[17],[12],[1],[20],[7],[6],[21],[2],[13],[16],[17],[6],[5],[10],[13],[10],[17],[0],[1],[8],[7],[4],[15],[14],[13],[0],[13],[0],[19],[18],[1],[20],[15],[0],[21],[18]]
expected = [None,None,None,None,None,None,None,None,None,None,None,False,False,True,False,None,False,True,True,False,None,False,None,False,False,None,True,False,True,False,False,False,False,True,True,None,None,None,None,False,False,None,None,False,True,False,False,False,None,None,True,False,False,None,False,False,False,False,False,True,True,False,False,False,True,True]

output = []
for f,arg in zip(input1,input2):
  output.append(eval(f'l.{f}({arg[0]})'))
  print(f, arg)
  print(l.toArray())
  if output != expected[:len(output)]:
    print(output[-1], expected[len(output)-1])
    break


# print(output == expected[:len(output)])
# print(output)

# print(random.random())

# print(l.getUpper(x).val)
