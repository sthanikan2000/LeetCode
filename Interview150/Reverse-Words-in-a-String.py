class Solution:
    def reverseWords(self, s: str) -> str:
        res = \\
        l=r=0
        n = len(s)
        while r<n:
            if s[r] == \ \ and l==r:
                l+=1
                r+=1
                continue
            if s[r] == \ \:
                if res:
                    res = s[l:r] + \ \ + res
                else:
                    res = s[l:r] + res
                r+=1
                l=r
                continue
            r+=1
            if r == n:
                if res:
                    res = s[l:r] + \ \ + res
                else:
                    res = s[l:r] + res
        return res

                




        