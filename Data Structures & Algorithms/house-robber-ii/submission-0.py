class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.robHouse(nums[1:]), self.robHouse(nums[:-1]))
# nums[0] in max(): if nums has only one element the elemt is the ans

    def robHouse(self, nums):
        rob1, rob2 = 0, 0
        for n in nums:
            temp = max(n+rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2