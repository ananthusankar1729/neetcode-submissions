class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l=set()
        for i in range(len(nums)-2):
            x = set()
            for j in range(i+1,len(nums)):
                k = -(nums[i]+nums[j])
                if k in x:
                    tup = tuple(sorted([nums[i],nums[j],k]))
                    l.add(tup)
                else:
                    x.add(nums[j])
        return list(l)
