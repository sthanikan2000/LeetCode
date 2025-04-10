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
        
        global_storage =  {\current\:None}
        def flat(root: Optional[TreeNode],storage):
            if not root:
                return
            root_l = root.left
            root_r = root.right
            current = storage[\current\]
            if current==None:
                current = root
                current.left = None
                current.right = None
                storage[\current\] = current
            else:
                current.right=root
                current = current.right
                current.left = None
                current.right = None
                storage[\current\] = current
            flat(root_l,storage)
            flat(root_r,storage)
        flat(root,global_storage)
        return root