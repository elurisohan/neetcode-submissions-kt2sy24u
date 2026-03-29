class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
            nums.sort()#nlogn
            res=[]
            for i in range(len(nums)-2):
                if nums[i]>0:
                    break

                if i>0 and nums[i]==nums[i-1]:
                    continue
                a=i+1
                b=len(nums)-1

                while a<b:
                    if nums[i]+nums[a]+nums[b]==0:
                        res.append([nums[i],nums[a],nums[b]])
                        a+=1
                        b-=1
                        while nums[a]==nums[a-1] and a<b:
                            a+=1
                    elif nums[i]+nums[a]+nums[b]<0:
                        a+=1
                    else:
                        b-=1
            return res