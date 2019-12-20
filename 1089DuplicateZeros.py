# arr = [1, 0, 2, 3, 0, 4, 5, 0]
# expected = [1, 0, 0, 2, 3, 0, 0, 4]
# test [1,2,3,0]
arr = [0]

i = 0
j = 0
while i < len(arr) and j < len(arr):
  if arr[i] == 0:
    j += 1
  j += 1
  i += 1

i -= 1
j -= 1

if j >= len(arr):
  arr[j-1] = arr[i]
  i -= 1
  j -= 2

for x in range(i, -1, -1):
  arr[j] = arr[x]
  j -= 1
  if arr[x] == 0 and j != len(arr)-1:
    arr[j] = arr[x]
    j -= 1


print(arr)
