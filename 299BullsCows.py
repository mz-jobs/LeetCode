from collections import Counter

secret = "1123999"
guess = "0011593"


bulls = sum([s == g for s, g in zip(secret, guess)])
sc = Counter(secret)
gc = Counter(guess)
cows = sum((sc & gc).values()) - bulls


print(bulls)
print(cows)
