class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for b in s:
            if b in [\(\,\{\,\[\]:
                stack.append(b)
                continue
            if not stack:
                return False
            if b == \)\ and stack[-1] != \(\:
                return False
            if b == \]\ and stack[-1] != \[\:
                return False
            if b == \}\ and stack[-1] != \{\:
                return False
            stack.pop()
        if stack:
            return False
        return True