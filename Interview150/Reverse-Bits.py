class Solution:
    def reverseBits(self, n: int) -> int:
        # bin_ = bin(n)[2:]
        # bin_ = [\0\]*(32-len(bin_))+list(bin_)
        
        # for i in range(0,16):
        #     bin_[i],bin_[31-i] = bin_[31-i],bin_[i]
        # return int(\\.join(bin_),2)  

        ######  ---------- Alternate solution using bit operations -----------------
        result = 0
        for _ in range(32):
            lsb = n & 1
            # result = (result<<1)+lsb
            result = (result<<1) | lsb 
            n = n >> 1
        return result

