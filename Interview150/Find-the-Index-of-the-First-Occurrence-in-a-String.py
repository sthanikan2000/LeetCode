class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        len_needle=len(needle)
        s=0
        len_haystack=len(haystack)
        while s+len_needle<=len_haystack:
            if haystack[s:s+len_needle]==needle:
                return s
            s+=1
        return -1

        
