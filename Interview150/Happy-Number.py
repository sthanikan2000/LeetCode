class Solution:
    
    def isHappy(self, n: int) -> bool:
        non_happy_cycle = {42, 37, 89, 20, 145, 16, 58, 4}
        n = str(n)
        while True:
            if n==1:
                return True
            if n in non_happy_cycle:
                return False
            n = sum([int(d)**2 for d in str(n)])
        