num1 = "1234567"
num2 = "123456789"

num1 = '0'*(max(len(num2)-len(num1), 0)+1) + num1
num2 = '0'*(max(len(num1)-len(num2), 0)+1) + num2

res = []
overflow = 0
for i, (n1, n2) in enumerate(zip(num1[::-1], num2[::-1])):
  print(i, n1, n2)
  x = int(n1) + int(n2) + overflow
  res.append(x % 10)
  overflow = int(x >= 10)

if res[-1] == 0:
  del res[-1]

print(''.join([str(i) for i in res[::-1]]))
