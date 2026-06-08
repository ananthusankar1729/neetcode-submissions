class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        
        def dfs(i, s):
            if len(s) == k:
                res.append(s)
                return
            if i > n:
                return
            dfs(i+1, s + [i])
            dfs(i+1, s)
        
        dfs(1, [])
        return res
            