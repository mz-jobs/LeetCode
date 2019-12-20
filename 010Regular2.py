

def isMatch(s: str, p: str) -> bool:
  import itertools

  def partitions(n, k):
    for c in itertools.combinations(range(n+k-1), k-1):
      yield [b-a-1 for a, b in zip((-1,)+c, c+(n+k-1,))]

  def comp(s, p):
    return len(s) == len(p) and all([i == j or j == '.' for i, j in zip(s, p)])

  n_stars = p.count('*')
  n_missing = len(s) - (len(p) - n_stars*2)
  # print(n_stars)
  # print(n_missing)
  p = p.split('*')

  # print(p, len(p))

  # l = list(combinations_with_replacement(range(len(p)-1), n_missing))
  # l = [x for x in product(range(n_missing+1), repeat=len(p)-1)
  #      if sum(x) == n_missing]

  # l = list(partitions(n_missing, n_stars))
  # print(l, len(l))
  # for c in l:
  if n_stars == 0:
    return comp(s, p[0])

  checked = set()
  print(len(list(partitions(n_missing, n_stars))))
  for c in partitions(n_missing, n_stars):
    fill = ''.join(
        [p_el[:-1] + p_el[-1] * n for p_el, n in zip(p, c)] + [p[-1]])
    # print(fill)

    if not fill in checked and comp(s, fill):
      print('MATCH **************')
      print(fill)
      print(s)
      return True

    checked.add(fill)

  print(len(checked))
  return False


s = "aasdfxasdfasdfasdfas"
p = "aasdf.*asdf.*asdf.*asdf.*s"

s = "aaaaaaaaaaaaab"
p = "a*a*a*a*a*a*a*a*a*a*a*a*b"

s = "bbabacccbcbbcaaab"
p = "a*b*a*a*c*aa*c*bc*"

x = isMatch(s, p)
print(x)

pass
