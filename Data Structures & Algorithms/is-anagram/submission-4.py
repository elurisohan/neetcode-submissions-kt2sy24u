class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        d1=[0]*27
        d2=[0]*27
        for i in range(len(s)):
            d1[ord('a')-ord(s[i])]+=1
            d2[ord('a')-ord(t[i])]+=1

        return d1==d2
        


