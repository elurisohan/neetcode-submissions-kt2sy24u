class TimeMap:

    def __init__(self):
        self.d={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.d:
            self.d[key].append([value,timestamp])
        else:
            self.d[key]=[[value,timestamp]]

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.d:
            return ''
        l=0
        h=len(self.d[key])-1
        ans=''
        while l<=h:
            mid=(l+h)//2        
            if self.d[key][mid][1]>timestamp:
                h=mid-1
            elif self.d[key][mid][1]<timestamp:
                ans=self.d[key][mid][0]
                l=mid+1
            else:
                ans=self.d[key][mid][0]
                return ans
        return ans