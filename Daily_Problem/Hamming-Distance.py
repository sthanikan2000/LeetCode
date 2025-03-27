class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        z  = x ^ y
        c = 0
        while z>0:
            if z & 1:
                c+=1
            z >>=1 
        return c
        