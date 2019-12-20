# from pycallgraph import PyCallGraph
# from pycallgraph.output import GraphvizOutput
# import cProfile
from line_profiler import LineProfiler
from typing import List

intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
# intervals = [[1, 4], [4, 5]]
# intervals = [[1, 4], [0, 4]]


def merge(intervals: List[List[int]]) -> List[List[int]]:
  if len(intervals) < 2:
    return intervals
  intervals.sort(key=lambda x: x[0])
  # sorted by x0
  res = [intervals[0]]

  for b in intervals[1:]:
    if b[0] <= res[-1][1]:  # overlapping if sorted
      if b[1] > res[-1][1]:
        res[-1][1] = b[1]
    else:
      res.append(b)
  return res


# print(merge(intervals))
def do_stuff():
  for _ in range(int(1e5)):
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    merge(intervals)


lp = LineProfiler()
lp_wrapper = lp(do_stuff)
lp.add_function(merge)
lp_wrapper()
lp.print_stats()
# with PyCallGraph(output=GraphvizOutput()):
#   for _ in range(100000):
#     intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
#     merge(intervals)


# cProfile.run("toProfile()")
