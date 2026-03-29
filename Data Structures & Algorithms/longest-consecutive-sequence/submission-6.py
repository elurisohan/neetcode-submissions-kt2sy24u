class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set=set((nums))
        long=0

        for i in nums:
            ans=1
            while i-1 in nums_set:
                ans+=1
                i-=1
            long=max(long,ans)
        
        return long


