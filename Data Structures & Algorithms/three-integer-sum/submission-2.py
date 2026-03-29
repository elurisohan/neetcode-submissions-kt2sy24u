class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort() #O(NlogN)

        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            
            x=i+1
            y=len(nums)-1

            while x<y:
                su=nums[i]+nums[x]+nums[y]
                if su==0:
                    res.append([nums[i],nums[x],nums[y]])
                    x+=1
                    y-=1

                    while x<y and nums[x]==nums[x-1]:
                        x+=1
                    while x<y and nums[y]==nums[y+1]:
                        y-=1
                    
                elif su<0:
                    x+=1
                else:
                    y-=1

                

        return res


