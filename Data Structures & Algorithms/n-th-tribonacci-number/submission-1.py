class Solution:
    def tribonacci(self, n: int) -> int:
        x, y, z = 0, 1, 1
        if n==0:
            return 0
        if n<=2:
            return 1
        for i in range(n-2):
            x, y, z = y, z, x+y+z
        return z