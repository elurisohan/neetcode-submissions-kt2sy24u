class Solution:
    def isValid(self, s: str) -> bool:
        dic= { ")" : "(", "]" : "[", "}" : "{" }

        stac=[]

        for i in s:
            if i not in dic :
                stac.append(i)

            elif i in dic and len(stac)!=0 and stac[-1]==dic[i]:
                stac.pop()
            
            else:#here this should return false for both conditions
                return False
        return len(stac)==0
