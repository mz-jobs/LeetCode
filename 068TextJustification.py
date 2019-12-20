words = ["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain",
         "to", "a", "computer.", "Art", "is", "everything", "else", "we", "do"]
maxWidth = 20

words = ["What", "must", "be", "acknowledgment", "shall", "be"]
maxWidth = 16

res = []

while words:
  x = maxWidth - len(words[0])
  line = [words.pop(0)]
  while words and 1+len(words[0]) <= x:
    line[-1] += ' '
    x -= 1+len(words[0])
    line.append(words.pop(0))

  if len(line) > 1:
    i = 0
    while i < x:
      line[i % (len(line)-1)] += ' '
      i += 1
  else:
    line[-1] += ' '*x

  res.append(''.join(line))

res[-1] = ' '.join(res[-1].split())
res[-1] += ' ' * (maxWidth-len(res[-1]))

print(res)
for line in res:
  print(line)
