class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(par, countl, countr):
            if countl==0 and countr==0 :
                res.append(par)
                return
            
            if countl > 0:
                dfs(par + "(", countl-1, countr)
            
            if countr > countl:
                dfs(par + ")", countl, countr-1)

        dfs("(", n-1, n)
        return res

            
            

                
