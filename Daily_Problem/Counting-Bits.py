class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        if n == 1:
            return [0,1]
        
        res = [0,1]
        bound = 1 << 1
        for i in range(2,n+1):
            if i == bound:
                res.append(1)
                bound <<= 1
            else:
                res.append(1+res[i-bound])
        return res





        