# https://leetcode.com/discuss/interview-experience/389969/google-l3-seattle-sep-2019-no-offer
# R3

from statistics import mean
from typing import Dict
d = list()
# for line in open('_sample.dict'):
for line in open('_words_alpha.txt'):
  d.append(line.split(maxsplit=1)[0])

d = list(filter(lambda w: not any([c in w for c in "'()."]), d))
d = list(filter(lambda w: len(w) > 2, d))

# print(d[:100])


class TrieNode:
  def __init__(self, x):
    self.val = x
    self.children = dict()
    self.terminal = None
    self.win_chance = None

  def add_word(self, s, full_word):
    if not s:
      self.terminal = full_word
      return
    if s[0] not in self.children.keys():
      self.children[s[0]] = TrieNode(s[0])

    self.children[s[0]].add_word(s[1:], full_word)
    return

  def get_node(self, s):
    if not s:
      return self
    return self.children[s[0]].get_node(s[1:])

  def get_win_chance(self):
    if self.terminal:
      self.win_chance = 0
      return 0
    self.win_chance = 1.0 - max([c.get_win_chance()
                                 for c in self.children.values()])
    return self.win_chance


t = TrieNode('')
# t.add_word('asd', 'asd')
for word in d:
  t.add_word(word, word)

print(t.children['c'].children['a'].children['b'].terminal)

print(t.get_win_chance())

for k, v in t.children.items():
  print(k, f'{v.win_chance:.3}')

print(t.get_node('c').win_chance)

print('*** GAME ***')
x = t
while not x.terminal:
  x = max(x.children.values(), key=lambda it: it.win_chance)
  print(x.val, x.win_chance)
