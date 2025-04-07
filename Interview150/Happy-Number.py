class Solution:
    def isHappy(self, n: int) -> bool:
        non_happy_cycle = {42:0, 37:0, 89:0, 20:0, 145:0, 16:0, 58:0, 4:0}
        while True:
            if n in non_happy_cycle:
                return False
            if n == 1:
                return True
            n =  sum([int(d)**2 for d in str(n)])
            
        '''
        def sumOfSquares_8th_iteration(x):
            for i in range(8):
                x = sum([int(d)**2 for d in str(x)])
            return x
        # prev_n = n
        # n = sum([int(d)**2 for d in str(x)]) 
        while True:
            if n == 1:
                return True
            prev_n = n
            n = sumOfSquares_8th_iteration(n)
            if n == prev_n:
                return False
        '''

        '''
        non_happy_cycle = {42, 37, 89, 20, 145, 16, 58, 4}
        n = str(n)
        while True:
            if n==1:
                return True
            if n in non_happy_cycle:
                return False
            n = sum([int(d)**2 for d in str(n)])
        '''
        