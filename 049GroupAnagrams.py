
# strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
d = {}
for s in strs:
  ss = ''.join(sorted(s))
  if ss not in d.keys():
    d[ss] = [s]
  else:
    d[ss].append(s)

print(list(d.values()))
