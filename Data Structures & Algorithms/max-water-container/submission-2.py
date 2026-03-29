class Solution:
    def maxArea(self, heights: List[int]) -> int:
        a=0
        b=len(heights)-1
        max_water=0

        while a<b:
            water=0
            if heights[a]<=heights[b]:
                water=heights[a]*(b-a)
                max_water=max(max_water,water)
                a+=1
            else:
                water=heights[b]*(b-a)
                max_water=max(max_water,water)
                b-=1
        return max_water
