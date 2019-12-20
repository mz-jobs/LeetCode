
# from typing import List
import typing


class Solution:
  def letterCombinations(self, digits: str) -> typing.List[str]:
    legend = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }

    pre = ['']
    for d in digits:
      post = []
      for p in pre:
        for l in legend[d]:
          post.append(p + l)
      pre = post

    return post


digits = "232"
legend = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyzs"
}
pre = ['']

for d in digits:
  post = []
  for p in pre:
    for l in legend[d]:
      post.append(p + l)
  pre = post
