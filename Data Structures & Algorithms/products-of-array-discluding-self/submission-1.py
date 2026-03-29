class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[1]*n

        for i in range(1,len(nums)):
            res[i]=nums[i-1]*res[i-1]


        postfix=1
        for i in range(len(nums)-1,-1,-1):
            res[i]*=postfix
            postfix=nums[i]*postfix

        return res

        