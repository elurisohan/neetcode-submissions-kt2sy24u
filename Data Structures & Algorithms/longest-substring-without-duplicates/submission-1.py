class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen=0
        for i in range(len(s)):
            ss=set()
            for j in range(i,len(s)):
                if s[j] in ss:
                    break
                ss.add(s[j])
            maxLen=max(maxLen,len(ss))
        return maxLen
            