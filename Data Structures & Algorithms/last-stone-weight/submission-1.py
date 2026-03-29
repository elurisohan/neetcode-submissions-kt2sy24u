class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap=[-i for i in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap)>1:
            a=heapq.heappop(maxHeap)
            b=heapq.heappop(maxHeap)
            if a<b:
                heapq.heappush(maxHeap,(a-b))
        
        return abs(maxHeap[0]) if maxHeap else 0