class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        ### Method 1
        s_to_t = {}
        assigned = []
        for i in range(len(s)):
            x = s_to_t.get(s[i])
            if x == None and t[i] not in assigned:
                s_to_t[s[i]] = t[i]
                assigned.append(t[i])
            elif x != t[i]:
                return False
        return True
        '''
        ### Method 2
        f_occ_1 = {}
        f_occ_2 = {}
        for i in range(len(s)):
            x = f_occ_1.get(s[i])
            y = f_occ_2.get(t[i])
            if  x == y == None:
                f_occ_1[s[i]] = i
                f_occ_2[t[i]] = i
            elif x != y:
                return False     
        return True
        '''