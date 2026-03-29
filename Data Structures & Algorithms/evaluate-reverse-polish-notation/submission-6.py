class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stac=[]

        for i in tokens:
            if i=='+':
                b=stac.pop()
                a=stac.pop()
                stac.append(b+a)
            elif i=='-':
                b=stac.pop()
                a=stac.pop()
                stac.append(a-b)
            elif i=='*':
                b=stac.pop()
                a=stac.pop()
                stac.append(b*a)
            elif i=='/':
                b=stac.pop()
                a=stac.pop()
                stac.append(int(a/b))
            else:
                stac.append(int(i))

        return stac[0]
                            