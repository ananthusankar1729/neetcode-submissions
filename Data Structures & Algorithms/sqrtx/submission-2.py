class Solution:
    def mySqrt(self, x: int) -> int:
        if x > 1:
            for i in range(x+1):
                if i*i <= x:
                    continue
                else:
                    return i-1
        else:
            return x
