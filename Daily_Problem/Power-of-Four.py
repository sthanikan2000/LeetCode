class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        x = 1
        while n>x:
            x <<= 2
        if  n==x:
            return True
        return False
