# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        total = 0
        queue = [(root,\\)]
        while queue:
            x,y = queue.pop(0)
            y += str(x.val)
            if not x.left and not x.right:
                total += int(y)
                continue
            
            if x.left:
                queue.append((x.left,y))
            if x.right:
                queue.append((x.right,y))
        return total

        