class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited={}
        
        for i,a in enumerate(nums):
            diff=target-a
            if diff in visited:
                return [visited[diff],i]

            visited[a]=i
        return False