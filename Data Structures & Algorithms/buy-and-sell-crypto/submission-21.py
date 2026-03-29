class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        a=0
        b=1
        max_p=0
        while b<=len(prices)-1:
            profit=prices[b]-prices[a]
            if profit>0:
                if profit> max_p:
                    max_p=profit
            else:
                a=b
            b+=1

        return max_p