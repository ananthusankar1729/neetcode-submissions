class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones)>1:
            x = max(stones)
            stones.remove(x)
            y = max(stones)
            stones.remove(y)
            if x>y:
                stones.append(int(x-y))
        if len(stones)==1:
            return stones[0]
        return 0
