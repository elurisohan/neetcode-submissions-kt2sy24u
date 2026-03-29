class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen=set(nums)
        longest=0
        for i in nums:
            a=0
            long=0
            if i-1 not in seen:
                while i+a in seen:
                    long+=1
                    a+=1
                longest=max(longest,long)
        return longest