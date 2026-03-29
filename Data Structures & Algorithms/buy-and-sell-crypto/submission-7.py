class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP=0

        i,j=0,1

        while i<j and j<len(prices):
            if prices[i]<=prices[j]:
                pro=prices[j]-prices[i]
                maxP=max(maxP,pro)
                j+=1
                

            else:
                i=j
                j+=1
        return maxP
            
        
        