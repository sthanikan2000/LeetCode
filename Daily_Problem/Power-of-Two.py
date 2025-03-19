class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        x = 1
        while n>x:
            x <<= 1
        return n == x
        