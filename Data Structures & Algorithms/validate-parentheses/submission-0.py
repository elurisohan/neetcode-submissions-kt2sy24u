from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        dic={')':'(','}':'{',']':'['}
        stac=deque()
        for i in s:
            if i in ('{','(','['):
                stac.append(i)
            elif len(stac)!=0 and stac[-1]==dic[i]:
                stac.pop()
            else:
                return False
        return True if not stac else False

        
        