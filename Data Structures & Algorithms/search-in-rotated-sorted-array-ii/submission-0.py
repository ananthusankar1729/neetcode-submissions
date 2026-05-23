class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums)-1
        while l<=r:
            m = (l+r)//2
            if nums[m]==target or nums[l]==target or nums[r]==target:
                return True
            elif nums[l] == nums[m] and nums[m] == nums[r]:
                # shrinking down the search space
                l = l+1
                r = r-1
                continue
            elif nums[l]<=nums[m]:
                # left half is sorted
                if nums[l]<=target and target<=nums[m]:
                    r = m-1
                else:
                    l = m+1
            else:
                # right half is sorted
                if nums[m]<=target and target<=nums[r]:
                    l = m+1
                else:
                    r = m-1
        return False

