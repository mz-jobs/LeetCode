name = "alex"
typed = "aaleex"


def isLongPressed(name, typed):

  if name == typed:
    return True

  if not name or not typed or name[0] != typed[0]:
    return False

  i = 1
  j = 1

  while i < len(name) and j < len(typed):
    if name[i] == typed[j]:
      i += 1
      j += 1
    elif typed[j] == typed[j-1]:
      j += 1
    else:
      break

  while j < len(typed) and typed[j] == typed[j-1]:
    j += 1

  return i == len(name) and j == len(typed)


print(isLongPressed(name, typed))
