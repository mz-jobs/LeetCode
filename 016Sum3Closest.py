

# nums = [0, 2, 1, -3]
# target = 1

# x = sum3closest(nums, target)
# print(x)


def threeSumClosest(nums, target):
  nums.sort()
  L = len(nums)

  best = sum(nums[:3])

  for a in range(L-2):
    b = a+1
    c = L-1
    while b < c:
      S = nums[a] + nums[b] + nums[c]
      if abs(S-target) < abs(best - target):
        best = S
      if S - target > 0:
        c -= 1
      else:
        b += 1

  return best


# print(threeSumClosest([0, 2, 1, -3], 1))


# nums = [6,-34,70,-43,1,-74,56,-18,-47,44,43,-96,-81,-65,68,60,-9,59,-52,32,61,41,31,56,94,-53,-94,-35,38,55,20,-12,40,-41,-38,-10,10,16,-42,85,-38,4,-18,72,-39,95,-73,-55,-43,-70,0,46,97,-84,-67,-5,-37,68,15,-78,31,-80,-44,-48,-28,-100,-97,-4,6,-29,-21,-76,10,46,-49,80,27,-16,92,-90,-82,-13,-67,70,37,79,34,-48,-65,70,-15,60,6,45,41,16,56,67,-79,28,2,39,28,-80,-13,-72,-97,-37,-8,-100,-83,-37,-77,26,74,-36,-28,-78,-95,-81,39,-1,-50,4,87,-39,-52,6,-13,-16,-53,-95,94,2,-61,61,-1,-68,-33,-76,-41,54,57,-54,-24,-55,88,-58,53,0,76,-46,56,-95,17,-74,50,84,-19,-9,39,20,46,40,38,-46,-68,57,38,-44,-53,80]
# target = 0
# assert threeSumClosest(nums,target) == 0


nums = [-1, 2, 1, -4]
target = 1
assert threeSumClosest(nums, target) == 2
