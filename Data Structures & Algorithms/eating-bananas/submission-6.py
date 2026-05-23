class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math
        l, r = 1, max(piles)
        x = max(piles)
        while l<=r:
            total = 0
            k = (l+r)//2
            for i in range(len(piles)):
                total += math.ceil((piles[i]/k))
            if total <= h:
                x = min(x, k)
                r = k-1
            else:
                l = k+1
        return x
