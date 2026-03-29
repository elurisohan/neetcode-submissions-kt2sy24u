class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if t=="":
            return ""

        countt={}

        for i in range(len(t)):
            countt[t[i]]=1+countt.get(t[i],0)

        l=r=0
        reslen,res=float("infinity"),[0,-1]

        have,need=0,len(countt)
        counts={}
        for r in range(len(s)):

            counts[s[r]]=1+counts.get(s[r],0)

            if s[r] in countt and countt[s[r]]==counts[s[r]]:
                have+=1
                
                while have==need:
                    if reslen>(r-l+1):
                        reslen=r-l+1
                        res=[l,r]

                    counts[s[l]]-=1
                    if s[l] in countt and counts[s[l]]<countt[s[l]]:
                        have-=1
                    l+=1
        l,r=res
        return s[l:r+1]
        


