class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        res = 0
        temp = len(nums)+1
        for r in range(len(nums)):
            res += nums[r]
            while res >= target:
                temp = min(temp, r-l+1)
                res -= nums[l]
                l += 1
        if temp == len(nums)+1:
            return 0
        else:
            return temp


            














