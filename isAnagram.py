def isAnagram(self, s: str, t: str) -> bool:
    return sorted(s)==sorted(t)
###
s="anagram"
t="nagaram"
isAnagram(s,t)