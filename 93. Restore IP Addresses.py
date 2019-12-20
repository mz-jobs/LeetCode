

s = "25525511135"
s = "010010"


def restoreIpAddresses(s: str):
  def gen_ip_blocks(s: str, n: int):
    if n == 0:
      if s:
        return []
      else:
        return [""]

    res = []
    for i in range(1, min(4, len(s)+1)):
      if (int(s[:i]) > 255) or (i > 1 and int(s[0]) == 0):
        continue
      for right in gen_ip_blocks(s[i:], n-1):
        res.append(s[:i] + '.' + right)
    return res

  return [r[:-1] for r in gen_ip_blocks(s, 4)]


print(restoreIpAddresses(s))
