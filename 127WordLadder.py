from typing import List
import collections
beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
# wordList = ["hot", "dot", "dog", "lot", "log"]
# def d1(a, b):
#   return sum(c1 != c2 for c1, c2 in zip(a, b))


# for w in wordList:
#   print(beginWord, w, d1(beginWord, w))

def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
  if endWord not in wordList:
    return []

  wordList.append(beginWord)
  connect = collections.defaultdict(set)

  for p in range(len(wordList[0])):
    d = collections.defaultdict(set)
    for i, w in enumerate(wordList):
      k = w[0:p]+w[p+1:]
      d[k].add(i)
    for i, w in enumerate(wordList):
      k = w[0:p]+w[p+1:]
      connect[i] |= d[k]

  for c in connect:
    connect[c].remove(c)

  # for c in connect:
  #   print(wordList[c])
  #   for d in connect[c]:
  #     print('   ', wordList[d])

  begin = wordList.index(beginWord)
  end = wordList.index(endWord)
  # print(begin, end)

  visited = {begin}
  horizon = [[begin]]
  result = []
  while horizon and not result:
    new_horizon = []
    for el in horizon:
      for c in connect[el[-1]]:
        if c not in visited:
          new_horizon.append(el + [c])
        if c == end:
          result.append(el+[c])
    for el in new_horizon:
      visited.add(el[-1])

    horizon = new_horizon

  return [[wordList[i] for i in r] for r in result]


result = findLadders(0, beginWord, endWord, wordList)
print(result)
