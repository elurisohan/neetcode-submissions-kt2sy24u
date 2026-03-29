class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stac=[]

        for i in range(len(tokens)):
            if tokens[i]=='+':
                b=int(stac.pop())
                a=int(stac.pop())
                stac.append(a+b)

            elif tokens[i]=='-':
                b=int(stac.pop())
                a=int(stac.pop())
                stac.append(a-b)
            elif tokens[i]=='*':
                b=int(stac.pop())
                a=int(stac.pop())
                stac.append(a*b)
            elif tokens[i]=='/':
                b=int(stac.pop())
                a=int(stac.pop())
                stac.append(a/b)
            else:
                stac.append(tokens[i])


        return int(stac[-1])
