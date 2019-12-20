

dividend = 7
divisor = -3

dividend = -2**31
divisor = -1


def divide(dividend: int, divisor: int) -> int:
  sign = 1
  if (dividend < 0) != (divisor < 0):  # XOR
    sign = -1
  if dividend < 0:
    dividend = -dividend
  if divisor < 0:
    divisor = -divisor

  n = 0
  x = divisor
  while x <= dividend:
    x += divisor
    n += 1

  if sign < 0:
    n = -n
  return n


x = divide(dividend, divisor)
print(x)
