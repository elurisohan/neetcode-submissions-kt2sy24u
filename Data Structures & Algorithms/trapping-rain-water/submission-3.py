class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height)<3:
            return 0

        lmax=height[0]
        rmax=height[len(height)-1]
        res=0
        l=0
        r=len(height)-1

        while l<r:
            if lmax<rmax:
                l+=1
                lmax=max(height[l],lmax)
                res+=lmax-height[l]
            else:
                r-=1
                rmax=max(rmax,height[r])
                res+=rmax-height[r]
        return res