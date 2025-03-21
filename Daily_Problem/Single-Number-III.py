class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor_all = 0
        for num in nums:
            xor_all ^= num
        
        # xor_all is the xor of two numbers(let x, y) with frequency 1
        # find the right most 1 bit in xor_all => that will be the first none same bit ind of x and y
        # so if we find that bit then, we can seperate numbers into two groups
        '''
        ### Method 1
        sep = 1
        while sep & xor_all == 0:
            sep <<= 1
        '''
        ### Method 2
        sep = xor_all & -xor_all
        
        res = [0,0]
        for num in nums:
            if num & sep == 0:
                res[0] ^= num
            else:
                res[1] ^= num
        return res
        



        