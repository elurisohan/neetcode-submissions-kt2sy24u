class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        a=0
        b=len(numbers)-1

        while a<b:
            val=numbers[a]+numbers[b]
            if val>target:
                b-=1
            elif val<target:
                a+=1
            else:
                return [a+1,b+1]
