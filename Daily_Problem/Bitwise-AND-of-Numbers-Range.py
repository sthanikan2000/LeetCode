class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        x=0
        while left and right and left != right:
            left >>= 1
            right >>= 1
            x += 1
        if left != right:
            return 0
        return left << x
        '''
        ### ---------- Solution with only bit operations and comparison - PASSED ALL Test cases ---------------------------------
        x = 1
        while left>=x and right>=x:
            x = x << 1
        if left>=x or right>=x:
            return 0
        
        # print(bin(x))

        res = 0
        while x:
            y = left & x
            z = right & x
            if y != z:
                break
            res = res | y
            x = x >> 1

        return res
        '''

        '''
        #### ------------------ Done by converting to string - PASSED ALL Test cases -------------------
        def int_to_bin_str(num):
            if num == 0:
                return \0\
            res = \\
            while num:
                res = str(num & 1) + res
                num = num >> 1
            return res
        
        def bin_str_to_int(s):
            int_ = 1
            for i in range(1,len(s)):
                if s[i] == \1\:
                    int_ = int_ << 1
                    int_ = int_ | 1
                else:
                    int_ = int_ << 1
            return int_

        b_r = int_to_bin_str(right)
        b_l = int_to_bin_str(left)

        if len(b_r) != len(b_l):
            return 0
        
        # print(b_r,b_l)

        if b_l == \0\:
            return 0

        s = \1\
        for i in range(1,len(b_r)):
            if b_r[i] == b_l[i]:
                s += b_r[i]
            else:
                s += \0\
                break
        # print(s)
                
        while  len(s) != len(b_r):
            s += \0\
        
        return bin_str_to_int(s)
        '''
