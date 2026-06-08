class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(i, s):
            if i==len(nums):
                res.append(s)
                return
            dfs(i+1, s)
            dfs(i+1, s+[nums[i]])

        dfs(0,[])
        return res
