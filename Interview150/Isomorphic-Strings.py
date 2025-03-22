class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        f_occ_1 = {}
        f_occ_2 = {}
        # lst = []
        for i in range(len(s)):
            x = f_occ_1.get(s[i])
            y = f_occ_2.get(t[i])
            if  x == None and y==None:
                # lst.append(i)
                f_occ_1[s[i]] = i
                f_occ_2[t[i]] = i
            elif x == y:
                continue
            else:
                return False
        # print(lst)

        
        return True