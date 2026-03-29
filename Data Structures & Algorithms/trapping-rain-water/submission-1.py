class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height)<3:
            return 0

        leftHeight=[0]*len(height)
        rightHeight=[0]*len(height)
        res=[0]*len(height)

        for i in range(1,len(height)):
            leftHeight[i]=max(height[i-1],leftHeight[i-1])

        for i in range(len(height)-2,-1,-1):
            rightHeight[i]=max(height[i+1],rightHeight[i+1])

        for i in range(len(height)):
            hi=min(leftHeight[i],rightHeight[i])
            if hi>height[i]:
                res[i]=hi-height[i] 

        return sum(res)