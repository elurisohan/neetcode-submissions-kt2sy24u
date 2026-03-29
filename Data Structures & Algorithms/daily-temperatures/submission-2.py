class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[0]*len(temperatures)
        stac=[]

        for i,t in enumerate(temperatures):
            while stac and stac[-1][1]<t:
                stacInd,stacTemp=stac.pop()
                res[stacInd]=i-stacInd
            stac.append((i,t))
        return res