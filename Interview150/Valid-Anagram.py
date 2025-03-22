class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        c_l = {}
        for c in s:
            x = c_l.get(c,0)
            c_l[c] = x+1
        for c in t:
            x = c_l.get(c,0)
            if x:
                c_l[c] = x-1
            else:
                return False
        return True
            