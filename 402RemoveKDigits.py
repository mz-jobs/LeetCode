# num = "1432219"
num = "50000005660469"
k = 3


def removeKdigits(num: str, k: int) -> str:
  num = list(num)

  i = 0
  for _ in range(k):
    while i < len(num)-1 and num[i] <= num[i+1]:
      i += 1

    del num[i]
    i -= 1
    if i < 0:
      i = 0
    while len(num) > 0 and num[0] == '0':
      del num[0]

    if len(num) == 0:
      return '0'

  return ''.join(num)


print(removeKdigits(num, k))
