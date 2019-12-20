from bisect import bisect_right


class SummaryRanges(object):

  def __init__(self):
    """
    Initialize your data structure here.
    """
    # self.intervals = []
    self.checked = set()
    self.starts = []
    self.stops = []

  def addNum(self, val):
    """
    :type val: int
    :rtype: None
    """
    if val in self.checked:
      return
    self.checked.add(val)

    i = bisect_right(self.starts, val)
    if i > 0 and self.stops[i-1]+1 == val and i < len(self.starts) and self.starts[i]-1 == val:
      self.stops[i-1] = self.stops[i]
      del self.starts[i]
      del self.stops[i]
    if i > 0 and self.stops[i-1]+1 >= val:
      if self.stops[i-1]+1 == val:
        self.stops[i-1] = val
    elif i < len(self.starts) and self.starts[i]-1 == val:
      self.starts[i] = val
    else:
      self.starts.insert(i, val)
      self.stops.insert(i, val)

    print(list(zip(self.starts, self.stops)))

  def getIntervals(self):
    """
    :rtype: List[List[int]]
    """
    return zip(self.starts, self.stops)


# intervals = []

# val = 3


# 1 can be merged with both
# 2 can be merged with left
#


# Your SummaryRanges object will be instantiated and called as such:
obj = SummaryRanges()
obj.addNum(1)
obj.addNum(3)
obj.addNum(3)
obj.addNum(7)
obj.addNum(2)
obj.addNum(6)
# param_2 = obj.getIntervals()
