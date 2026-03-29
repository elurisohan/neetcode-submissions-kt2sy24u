class Solution:
    def isValid(self, s: str) -> bool:
        dic={')':'(',']':'[','}':'{'}
        stac=[]
        for i in s:
            if i in dic.values():
                stac.append(i)
            elif i in dic and not stac:
                return False
            elif i in dic and stac[-1]==dic[i]:
                stac.pop()
            else:
                return False

        return True if not stac else False