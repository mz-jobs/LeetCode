s = "Hello World"


def lengthOfLastWord(self, s: str) -> int:
  return len(s.strip().split(' ')[-1])
