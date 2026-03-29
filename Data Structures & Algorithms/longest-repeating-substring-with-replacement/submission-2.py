class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashMap={}
        l=0
        maxLen=0
        for r in range(len(s)):
            hashMap[s[r]]=1+hashMap.get(s[r],0)
            while (r-l+1-max(hashMap.values()))>k:
                hashMap[s[l]]-=1
                l+=1
                
            maxLen=max(maxLen,r-l+1)
        return maxLen


        
