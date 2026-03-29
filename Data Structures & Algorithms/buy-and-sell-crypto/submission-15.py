class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        a=0
        b=1
        profit=0

        if len(prices)==1:
            return profit 
        while b<len(prices):
            if prices[a]<=prices[b]:
                profit=max(profit,prices[b]-prices[a])
                b+=1
            else:
                a=b
                b+=1
        return profit
