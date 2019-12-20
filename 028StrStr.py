haystack = "hello"
needle = "el"


def find(haystack, needle):
  for i in range(len(haystack)-len(needle)+1):
    j = 0
    while j < len(needle) and haystack[i+j] == needle[j]:
      j += 1
    if j == len(needle):
      return i
  return -1


print(find(haystack, needle))

print(haystack.find(needle))
