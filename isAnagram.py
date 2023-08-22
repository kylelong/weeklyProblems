def isAnagram(s, t):
    if len(s) != len(t): return False
    for i in range (ord('a'), ord('z') + 1):
        letter = chr(i)
        if s.count(letter) != t.count(letter): return False
    return True
print(isAnagram('barbie', 'oppenheimer')) # False
print(isAnagram('race', 'care')) # True