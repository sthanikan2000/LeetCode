# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def depthLeftMost(root):
            current = root
            d = 0
            while current.left:
                d+=1
                current = current.left
            return d
        def depthRightMost(root):
            current = root
            d = 0
            while current.right:
                d+=1
                current = current.right
            return d
        d_l = depthLeftMost(root)
        d_r = depthRightMost(root)
        if d_l == d_r:
            return ( 1 << (d_l + 1) ) - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

