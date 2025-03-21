class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s: 
            return True
        # len_t = len(t)
        len_s = len(s)
        i_s = 0
        for i in t:
            if i == s[i_s]:
                i_s+=1
                if i_s == len_s:
                    return True
        return False