class Solution():
    def hasDuplicate(self, nums):
        for i in range(0,len(nums)-1):
            for n in range(i+1, len(nums)):
                if nums[i]==nums[n]:
                    return True
                    break
        return False

         