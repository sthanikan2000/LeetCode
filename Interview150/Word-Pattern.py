class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_sp = s.split()
        if len(pattern) != len(s_sp):
            return False
        p_to_s = {}
        assigned = []
        for i in range(len(pattern)):
            x = p_to_s.get(pattern[i])
            if x == None and s_sp[i] not in assigned:
                assigned.append(s_sp[i])
                p_to_s[pattern[i]] = s_sp[i]
            elif x != s_sp[i]:
                return False
        return True


