# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ### Depth First Search
        i = 0
        stack = [root]
        while stack:
            x = stack.pop()
            if not x.left and not x.right:
                i+=1
                if i == k:
                    return x.val
                continue
            if x.right:
                stack.append(x.right)
                x.right = None
            temp = x.left
            if temp:
                x.left = None
            stack.append(x)
            if temp:
                stack.append(temp)

            
        