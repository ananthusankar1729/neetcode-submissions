class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, s):
            if sum(s)==target:
                res.append(s)
                return
            if sum(s)>target:
                return
            if i>len(nums)-1:
                return 
            
            dfs(i, s+[nums[i]])
            dfs(i+1, s)

        dfs(0, [])
        return res