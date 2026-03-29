class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        hashMapOne=[0]*26
        hashMapTwo=[0]*26
        for i in range(len(s)):
            hashMapOne[ord(s[i])-ord('a')]+=1
            hashMapTwo[ord(t[i])-ord('a')]+=1

        return hashMapOne==hashMapTwo

        