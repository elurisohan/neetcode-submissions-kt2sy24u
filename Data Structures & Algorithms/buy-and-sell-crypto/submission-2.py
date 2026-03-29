class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        x=0
        prof=profit=0
        for y in range(1,len(prices)):
            if prices[x]<=prices[y]:
                profit=prices[y]-prices[x] 
                prof=max(profit,prof)  
            else: 
                x=y

            
        return prof
        
        