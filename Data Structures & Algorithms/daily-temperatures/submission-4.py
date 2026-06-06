class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[0]*len(temperatures)

        stac=[]


        for i,val in enumerate(temperatures):
            while stac and temperatures[i]>stac[-1][1]:
                day,temp=stac.pop()
                res[day]=i-day
            
            stac.append([i,val])

        return res