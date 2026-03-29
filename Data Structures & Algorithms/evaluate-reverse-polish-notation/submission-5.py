class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stac=[]

        for i in tokens:
            if i =="+":
                a=stac.pop()
                b=stac.pop()
                stac.append(a+b)
            elif i =="-":
                a=stac.pop()
                b=stac.pop()
                stac.append(b-a)
            elif i =="*":
                a=stac.pop()
                b=stac.pop()
                stac.append(a*b)
            elif i =="/":
                a=stac.pop()
                b=stac.pop()
                stac.append(int(b/a))
            else:
                stac.append(int(i))
        
        return stac[0]