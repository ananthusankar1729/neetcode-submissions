class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i, s):
            if sum(s) == target:
                res.append(s)
                return
            if sum(s) > target or i>=len(candidates):
                return
            dfs(i+1, s+[candidates[i]])
            while i+1<len(candidates) and candidates[i]==candidates[i+1]:
                i+=1
            dfs(i+1, s)

        dfs(0, [])
        return res
