class MinStack:

    def __init__(self):
        self.stac=[]
        self.minStac=[]

    def push(self, val: int) -> None:
        self.stac.append(val)
        if len(self.minStac)>0 and self.minStac[-1]<val:
            minS=self.minStac[-1]
            self.minStac.append(minS)
        else:
            self.minStac.append(val)


    def pop(self) -> None:
        self.stac.pop()
        self.minStac.pop()

    def top(self) -> int:
        return self.stac[-1]

    def getMin(self) -> int:
        return self.minStac[-1]        
