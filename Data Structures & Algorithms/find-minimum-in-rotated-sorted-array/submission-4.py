class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        h=len(nums)-1

        while l<h:
            mid=(l+h)//2
            #if min in left of mid. arr[0]>mid
            #if min in right of mid mid>arr[1]
            if nums[l]<nums[h]:
                return nums[l]  
        
            elif nums[0]>nums[mid]:
                h=mid
            elif nums[l]<=nums[mid]:
                l=mid+1
        return nums[l]
   



    