input = ["My dog eats food",
         "She eats food too",
         "My dog food is good good"]


seen = set()
twice = set()

for line in input:
  current = set(line.split())
  twice |= seen & current
  seen |= current

print(seen - twice)
print(twice)
