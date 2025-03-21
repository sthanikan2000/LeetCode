class Solution:
    def simplifyPath(self, path: str) -> str:
        path_l = path.split(\/\)
        stack = []
        for dir in path_l:
            if dir == \\ or dir == \.\:
                continue
            elif dir == \..\:
                if stack:
                    stack.pop()
            else:
                stack.append(dir)
        return \/\ + \/\.join(stack)    
        