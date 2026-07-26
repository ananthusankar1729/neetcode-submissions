class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        l, r = 0, 1
        while l<len(nums):
            while r<len(nums):
                if nums[l]==nums[r]:
                    return nums[l]
                    break
                else:
                    r += 1
            l += 1
            r = l+1
 
