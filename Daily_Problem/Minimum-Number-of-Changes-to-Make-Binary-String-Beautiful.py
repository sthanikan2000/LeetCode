class Solution:
    def minChanges(self, s: str) -> int:
        ### Solution 1
        # return sum([1 for i in range(0,len(s),2) if s[i]!=s[i+1]])

        ## Solution 2
        changes = 0
        for i in range(0,len(s),2):
            if s[i] != s[i+1]:
                changes+=1
        return changes
        