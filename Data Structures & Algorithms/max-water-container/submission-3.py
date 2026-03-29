class Solution:
    def maxArea(self, heights: List[int]) -> int:
        x=0
        y=len(heights)-1
        water=0
        while x<y:
            wa=self.calc(x,y,heights)
            water=max(water,wa)
            if heights[x]<heights[y]:
                x+=1
            else:
                y-=1

        return water

    def calc(self,a,b,heights):
        return (b-a)*min(heights[a],heights[b])