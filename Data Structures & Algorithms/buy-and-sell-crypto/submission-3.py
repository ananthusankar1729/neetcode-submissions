class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # profit = []
        # for i in range(len(prices)-1):
        #     for j in range(i+1,len(prices)):
        #         prof = prices[j] - prices[i]
        #         if prof >= 0:
        #             profit.append(prof)
        # if len(profit) > 0:
        #     return max(profit)
        # else:
        #     return 0
        profit = 0
        b= 0
        while b<len(prices):
            for s in range(b, len(prices)):
                profit = max(profit, prices[s]-prices[b])
            b+=1
        return profit    