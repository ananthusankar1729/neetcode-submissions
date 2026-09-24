class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        incom = defaultdict(int)
        outgo = defaultdict(int)

        for src, dst in trust:
            outgo[src] += 1
            incom[dst] += 1

        for i in range(1, n+1):
            if incom[i]==n - 1 and outgo[i]==0:
                return i
        return -1