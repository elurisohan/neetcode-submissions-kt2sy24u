class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap=[]
        
        for i in points:
            dist=i[0]**2+i[1]**2
            heapq.heappush(minHeap,(dist,i))

        res=[]
        while len(res)<k:
            res.append(heapq.heappop(minHeap)[1])

        return res