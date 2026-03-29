class MinStack:

    def __init__(self):
        self.stac=[]
        self.minstac=[]

    def push(self, val: int) -> None:
        self.stac.append(val)
        if not self.minstac:
            self.minstac.append(val)
            
        elif self.minstac and val<self.minstac[-1]:
            self.minstac.append(val)
        else:
            self.minstac.append(self.minstac[-1])

    def pop(self) -> None:
        self.stac.pop()
        self.minstac.pop()
        
    def top(self) -> int:
        return self.stac[-1]

    def getMin(self) -> int:
       return self.minstac[-1]
        
