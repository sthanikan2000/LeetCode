class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
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
        ######### Failing many test cases
        # if (left << 1) <= right:
        #     return 0
        y = 1
        while y<left:
            y = y << 1
            y = y | 1
        print(bin(y))

        z = 1
        while z<right:
            z = z<<1
            z = z | 1
        print(bin(z))

        if y != z:
            return 0

        # odd_r = right & 1
        # odd_l = left & 1

        diff = right - left
        print(bin(diff))

        if diff & 1 and left & 1: # diff is odd and left is odd
            x = 10
        else:
            x = 1


        while diff>=x:
            y = y ^ x
            # if y != temp_y:

            x = x << 1
        print(bin(y))

        return z & left
        '''



        
        