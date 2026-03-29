class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen=set()

        long=0

        a=0
       
        for b in s:
            if b in seen:
                while b in seen:
                    seen.remove(s[a])
                    a+=1
            seen.add(b)
            long=max(long,len(seen))


        return long
