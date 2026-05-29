class MinStack:

    def __init__(self):
        self.stac1=[]
        self.stac2=[]

    def push(self, val: int) -> None:
        self.stac1.append(val)
        if self.stac2:
            if  self.stac2[-1]>val:
                self.stac2.append(val)
            else:
                value=self.stac2[-1]
                self.stac2.append(value)
        else:
            self.stac2.append(val)

    def pop(self) -> None:
        self.stac2.pop()
        self.stac1.pop()

    def top(self) -> int:
        return self.stac1[-1]

    def getMin(self) -> int:
        return self.stac2[-1]
