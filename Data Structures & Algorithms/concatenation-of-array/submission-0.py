class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        i = 0
        ans = []
        while i < 2*len(nums):
            if i<len(nums):
                ans.append(nums[i])
            else:
                ans.append(nums[i-len(nums)])
            i+=1
        return ans
