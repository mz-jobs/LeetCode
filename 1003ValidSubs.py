S = "abcabcababcc"

L = len(S)
S = S.replace('abc', '')
while len(S) < L:
  L = len(S)
  S = S.replace('abc', '')

return not S


print(S)
