class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a=0
        seen=set()
        maxy=0

        for b in range(len(s)):
            while s[b] in seen:
                seen.remove(s[a])
                a+=1
            seen.add(s[b])
            maxy=max(maxy,b-a+1)
        return maxy
