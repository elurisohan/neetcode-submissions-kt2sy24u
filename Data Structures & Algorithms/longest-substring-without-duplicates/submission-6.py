class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet=set(())
        a=b=0
        ans=0

        while b<len(s):
            while s[b] in charSet:
                charSet.remove(s[a])
                a+=1
            charSet.add(s[b])
            ans=max(ans,b-a+1)
            b+=1
        return ans