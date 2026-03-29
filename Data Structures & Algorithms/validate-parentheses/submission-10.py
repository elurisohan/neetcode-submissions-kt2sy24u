class Solution:
    def isValid(self, s: str) -> bool:
        hashMap={']':'[','}':'{',')':'('}

        stac=[]

        for i in s:
            if i in hashMap.values():
                stac.append(i)
            elif stac and stac[-1]==hashMap[i] :
                    stac.pop()
            else:
                return False
            
        return len(stac)==0
        
        
