from collections import Counter

# def canConstruct(ransomNote, magazine):


ransomNote = "aa"
magazine = "aab"

c1 = Counter(magazine)
c2 = Counter(ransomNote)
c1.subtract(c2)
print(c1.values())
print(all([i >= 0 for i in c1.values()]))
