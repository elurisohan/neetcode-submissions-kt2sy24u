class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqCount={}

        for i in nums:
            freqCount[i]=1+freqCount.get(i,0)

        bucketMap=[[] for i in range(len(nums)+1)]


        for i,cnt in freqCount.items():
            bucketMap[cnt].append(i)

        res=[]
        for j in range(len(bucketMap)-1,0,-1):
            for n in bucketMap[j]:
                res.append(n)
                if len(res)==k:
                    return res