class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen=set(nums)
        maxLen=0
        for i in nums:
            curr,streak=i,0
            while curr in seen:
                streak+=1
                curr+=1
            maxLen=max(streak,maxLen)

        return maxLen