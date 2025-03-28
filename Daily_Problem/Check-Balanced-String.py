class Solution:
    def isBalanced(self, num: str) -> bool:
        s1 = 0
        s2 = 0
        n = len(num)
        for i in range(1,n,2):
            s1+=int(num[i-1])
            s2+=int(num[i])
        if n%2 ==1:
            s1+=int(num[n-1])
        return s1 == s2
