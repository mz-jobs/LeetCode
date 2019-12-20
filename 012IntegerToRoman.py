romans = [
    ('I', 1),
    ('IV', 4),
    ('V', 5),
    ('IX', 9),
    ('X', 10),
    ('XL', 40),
    ('L', 50),
    ('XC', 90),
    ('C', 100),
    ('CD', 400),
    ('D', 500),
    ('CM', 900),
    ('M', 1000),
]

num = 3


def intToRoman(num):
  res = ''
  for sym, val in romans[::-1]:
    while num-val >= 0:
      num -= val
      res += sym

  return res


print(intToRoman(3))
print(intToRoman(4))
print(intToRoman(9))
print(intToRoman(58))
print(intToRoman(1994))
