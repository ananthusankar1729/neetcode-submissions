class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        l = []
        n = len(nums)
        num = set(nums)
        print(num)
        for i in num:
            if nums.count(i)>n/3:
                l.append(i)

        return l