class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap=[]

        for i in stones:
            heapq.heappush(maxHeap,-i)

        while len(maxHeap)>=2:
            a=heapq.heappop(maxHeap)
            b=heapq.heappop(maxHeap)

            if abs(a)==abs(b):
                continue

            if abs(a)>abs(b):
                heapq.heappush(maxHeap,(a-b))

        
        if maxHeap:
            return -maxHeap[0]
        return 0