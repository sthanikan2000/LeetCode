class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        a_and_b  = a & b
        a_or_b = a | b
        a_or_b_xor_c = a_or_b ^ c
        
        c = 0
        while a_or_b_xor_c>0:
            if a_or_b_xor_c & 1:
                if a_or_b & 1 == 1 and a_and_b & 1 ==1:
                    c+=2
                else:
                    c+=1
                    # if a_or_b & 1 == 1 and a_and_b & 1 ==0    <- POSSIBLE
                    # if  a_or_b & 1 == 0 and a_and_b & 1 ==0   <- POSSIBLE
                    # if a_or_b & 1 == 1 and a_and_b & 1 == 1   <- NEVER POSSIBLE
            a_and_b >>= 1
            a_or_b >>= 1
            a_or_b_xor_c >>= 1
        return c

        