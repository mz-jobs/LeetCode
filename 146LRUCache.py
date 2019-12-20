import collections


class DLListNode:
  def __init__(self, val, key):
    self.val = val
    self.key = key
    self.prev = None
    self.next = None


class DLList:
  def __init__(self):
    self.head = DLListNode(0, 0)
    self.tail = DLListNode(0, 0)
    self.head.prev = self.tail
    self.tail.next = self.head

  def push_front(self, node):
    node.prev = self.head.prev
    node.next = self.head
    self.head.prev.next = node
    self.head.prev = node

  def pop_back(self):
    if self.tail.next == self.head:
      return None
    x = self.tail.next
    self.tail.next = self.tail.next.next
    self.tail.next.prev = self.tail
    return x

  def move_front(self, node):
    node.prev.next = node.next
    node.next.prev = node.prev
    self.push_front(node)


class LRUCache:

  def __init__(self, capacity: int):
    self.dllist = DLList()
    self.d = {}
    self.capacity = capacity

  def get(self, key: int) -> int:
    if key not in self.d:
      # print(-1)
      return -1
    self.dllist.move_front(self.d[key])
    # print(self.d[key].val)
    return self.d[key].val

  def put(self, key: int, value: int) -> None:
    if key in self.d:
      self.dllist.move_front(self.d[key])
      self.d[key].val = value
    else:
      if len(self.d) >= self.capacity:
        x = self.dllist.pop_back()
        del self.d[x.key]
      self.d[key] = DLListNode(value, key)
      self.dllist.push_front(self.d[key])


    # Your LRUCache object will be instantiated and called as such:
    # obj = LRUCache(capacity)
    # param_1 = obj.get(key)
    # obj.put(key,value)
cache = LRUCache(2)

cache.put(1, 1)
cache.put(2, 2)
cache.get(1)
# // returns 1
cache.put(3, 3)
# // evicts key 2
cache.get(2)
# // returns - 1 (not found)
cache.put(4, 4)
# // evicts key 1
cache.get(1)
# // returns - 1 (not found)
cache.get(3)
# // returns 3
cache.get(4)
# // returns 4
