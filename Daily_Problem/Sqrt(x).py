class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        if x == 1:
            return 1
        s = 1
        e = x//2
        while s<=e:
            mid = (s+e)//2
            if mid**2 == x:
                return mid
            if (mid)**2 < x:
                s = mid+1
            else:
                e = mid-1
        return e

        