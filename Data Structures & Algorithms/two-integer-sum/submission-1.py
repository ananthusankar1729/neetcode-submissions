class Solution:
    def twoSum(self, nums, target):
        for n in range(0,len(nums)-1):
            for i in range(n+1, len(nums)):
                if nums[n] + nums[i] == target:
                    return [n,i]
        