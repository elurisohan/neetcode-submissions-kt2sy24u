class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        a=0
        profit=0

        for b in range(1,len(prices)):
            if prices[b]>prices[a]:
                pro=prices[b]-prices[a]
                profit=max(pro,profit)
            else:
                a=b
                

        return profit

