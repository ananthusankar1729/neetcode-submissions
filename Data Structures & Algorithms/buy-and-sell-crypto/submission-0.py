class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = []
        for i in range(len(prices)-1):
            for j in range(i+1,len(prices)):
                prof = prices[j] - prices[i]
                if prof >= 0:
                    profit.append(prof)
        if len(profit) > 0:
            return max(profit)
        else:
            return 0