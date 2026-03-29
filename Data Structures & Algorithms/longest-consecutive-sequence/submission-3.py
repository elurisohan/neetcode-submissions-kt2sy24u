class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen=set(nums)
        long=0
        for i in seen:
            longest=0
            if i-1 not in seen:
                while i in seen:
                    i+=1
                    longest+=1
            long=max(long,longest)
        return long