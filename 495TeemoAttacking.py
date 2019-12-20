x = [1, 2]
d = 2


def findPoisonedDuration(timeSeries, duration):
  if not timeSeries:
    return 0

  total = duration  # last attack
  for i in range(1, len(timeSeries)):
    if timeSeries[i] > timeSeries[i-1] + duration:
      total += duration
    else:
      total += timeSeries[i]-timeSeries[i-1]

  return total


print(findPoisonedDuration(x, 2))
