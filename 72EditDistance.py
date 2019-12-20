import functools
word1 = "horse"
word2 = "ros"

word1 = "intention"
word2 = "execution"

i1 = 0
i2 = 0


@functools.lru_cache()
def distance(w1, w2):
  if not w1:
    return len(w2)

  if not w2:  # empty second
    return len(w1)

  if w1[0] == w2[0]:
    return distance(w1[1:], w2[1:])
  else:
    return 1 + min([
        distance(w1[1:], w2[1:]),
        distance(w1[1:], w2),
        distance(w1, w2[1:])
    ])


x = distance(word1, word2)
print(x)
