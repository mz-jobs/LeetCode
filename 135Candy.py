ratings = [1, 2, 2]

ratings = [5]


def candy(ratings):
  N = len(ratings)
  left = [1]*N
  for i in range(1, N):
    if ratings[i] > ratings[i-1]:
      left[i] = left[i-1]+1

  right = [1]*N
  for i in range(N-2, -1, -1):
    if ratings[i] > ratings[i+1]:
      right[i] = right[i+1]+1

  return sum(map(max, zip(left, right)))


print(candy(ratings))
