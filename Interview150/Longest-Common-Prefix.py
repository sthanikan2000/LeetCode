# use the knowleadge of Trie
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        x=strs[0]
        for i in range(1,len(strs)):
            if not x:
                return \\
            if len(x) > len(strs[i]):
                    x=x[:len(strs[i])]
            for j in range(len(strs[i])):
                if j >= len(x):
                    x=x[:j]
                elif strs[i][j] != x[j]:
                    x=x[:j] 
                                  
        return x

        