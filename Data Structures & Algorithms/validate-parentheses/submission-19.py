class Solution:
    def isValid(self, s: str) -> bool:
        hm={')':'(',']':'[','}':'{'}

        stac=[]

        for i in s:
            if not stac :
                if i in hm:
                    return False
                else:
                    stac.append(i)

            elif i in hm and hm[i]==stac[-1] :
                stac.pop()
            
            else:
                stac.append(i)
        
        return len(stac)==0