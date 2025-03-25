class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        mapping = {}
        count = 0

        for i in range(len(s)):
            x = mapping.get(s[i],-1)
            if x == -1:
                mapping[s[i]]=i
                count+=1
                if count>max_len:
                    max_len=count
            else:
                for j in range(i-count,x):
                    mapping[s[j]]= -1
                count = i-x
                mapping[s[i]]=i
        return max_len

        