class Solution:
    def maxArea(self, heights: List[int]) -> int:
        water=0


        a=0
        b=len(heights)-1

        while a<b:
            wat=0
            wat=min(heights[a],heights[b])*(b-a)
            water=max(water,wat)
            if heights[a]<heights[b]:
                a+=1
            else:
                b-=1
        return water