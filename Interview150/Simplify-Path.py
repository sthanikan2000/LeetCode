class Solution:
    def simplifyPath(self, path: str) -> str:
        path_l = path.split(\/\)
        stack = []
        for dir in path_l:
            if dir == \\ or dir == \.\:
                continue
            elif dir == \..\:
                if not stack:
                    continue
                else:
                    stack.pop()
            else:
                stack.append(dir)
        if not stack:
            return \/\
        red = \/\ + \/\.join(stack)
        # if len(stack) == 1:
        #     return red + \/\
        return red
    
        