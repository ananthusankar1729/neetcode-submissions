class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prof = 0
        l, r = 0, 1
        while r<len(prices):
            if prices[r]>prices[l]:
                prof += prices[r]-prices[l]
                l = r
                r = l+1
            else:
                l+=1
                r+=1
        return prof