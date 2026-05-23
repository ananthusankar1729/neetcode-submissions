class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        res = 0
        l = 0
        r = len(nums)-1
        while l<=r:
            mid = (l+r)//2
            if nums[mid] == target :
                return mid
            elif nums[mid] < target :
                l = mid +1
                res = mid + 1
            else:
                r = mid -1
        return res







