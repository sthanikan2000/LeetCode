class Solution:
    def trailingZeroes(self, n: int) -> int:
        c = 0
        x = 5
        while x<=n:
            c += (n//x)
            x *= 5
        return c
        