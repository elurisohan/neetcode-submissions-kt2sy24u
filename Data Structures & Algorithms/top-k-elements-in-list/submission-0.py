class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map={}
        for i in nums:
            freq_map[i]=1+freq_map.get(i,0)

        min_heap=[]
        for num,coun in freq_map.items():
            heapq.heappush(min_heap,(coun,num))
            while len(min_heap)>k:
                heapq.heappop(min_heap)

        
        return [n for i,n in min_heap]

        