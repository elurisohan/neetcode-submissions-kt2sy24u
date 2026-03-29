class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        se=set()
        a=b=0
        maxi=0

        for b in range(len(s)):
            while s[b] in se:
                se.remove(s[a])
                a+=1
            se.add(s[b])
            maxi=max(maxi,b-a+1)

        return maxi