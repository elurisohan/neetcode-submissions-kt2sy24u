class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans =0

        a=0 
        b= len(heights)-1


        while a < b :
            ans = max(ans, (b-a)*min(heights[a],heights[b]))
            if heights[a]<heights[b]:
                a+=1
            else:
                b-=1
        return ans

    