class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        fre={}
        fmax=0
        l=0
        maxLen=0
        for r in range(len(s)):
            fre[s[r]]=1+fre.get(s[r],0)
            fmax=max(fmax,fre[s[r]])
            while (r-l+1)-fmax>k:
                fre[s[l]]-=1
                l+=1
            maxLen=max(maxLen,r-l+1)
        return maxLen
