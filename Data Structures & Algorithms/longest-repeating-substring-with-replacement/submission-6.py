class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        a=b=0
        maxf=0
        dic={}
        res=0

        while b<len(s):
            dic[s[b]]=1+dic.get(s[b],0)
            maxf=max(maxf,dic[s[b]])

            while (b-a+1)-maxf>k:
                dic[s[a]]-=1
                a+=1
            res=max(res,b-a+1)    
            b+=1

        return res
            
            