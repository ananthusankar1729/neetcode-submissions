class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMin, curMax = 1, 1
        res = float('-inf')
        for n in nums:
            # edge case: when an element is 0 
            # if n == 0 :
            #     curMin, curMax = 1, 1
            #     continue
            tmp = curMax
            curMax = max(n*curMax, n*curMin, n)
            curMin = min(n*curMin, n*tmp, n)
            res = max(res, curMax)
        return res
                