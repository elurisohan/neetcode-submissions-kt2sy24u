class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxWater=0
        l=0
        r=len(heights)-1

        while l<r:
            if heights[l]<=heights[r]:
                water=(r-l)*min(heights[l],heights[r])
                maxWater=max(water,maxWater)
                l+=1

            else:
                water=(r-l)*min(heights[l],heights[r])
                maxWater=max(water,maxWater)
                r-=1
        return maxWater