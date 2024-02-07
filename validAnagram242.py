
def isAnagram(s, t):
    return True if sorted(t) == sorted(s) else False         
print(isAnagram("anagram","nagaram"))