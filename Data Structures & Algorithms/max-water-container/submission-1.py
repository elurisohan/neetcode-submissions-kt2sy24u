class Solution:
    def maxArea(self, heights: List[int]) -> int:
        a=0
        b=len(heights)-1
        max_area=0
        while a<b:
            area=min(heights[a],heights[b])*(b-a)
            max_area=max(max_area,area)

            if heights[a]<=heights[b]:
                a+=1
            else:
                b-=1

        return max_area

    