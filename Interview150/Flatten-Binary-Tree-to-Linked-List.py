# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        \\\
        Do not return anything, modify root in-place instead.
        \\\
        if not root:
            return
        root_l = root.left
        root_r = root.right

        current = [root]
        current[0].left = None
        current[0].right = None
        def flat(root: Optional[TreeNode],current):
            root_l = root.left
            root_r = root.right
            
            current[0].right = root
            current[0] = current[0].right
            current[0].left=None
            current[0].right=None
            if root_l:
                flat(root_l,current)
            if root_r:
                flat(root_r,current)
        if root_l:
            flat(root_l,current)
        if root_r:
            flat(root_r,current)
        return root