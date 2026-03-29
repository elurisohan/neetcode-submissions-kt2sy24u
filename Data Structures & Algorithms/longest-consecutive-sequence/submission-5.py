class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset=set(nums)
        maxseq=0
        for i in nums:
            if i-1 not in numset:
                seq=1
                while i+1 in numset:
                    seq+=1
                    i+=1
                maxseq=max(maxseq,seq)
            else:
                continue
        return maxseq