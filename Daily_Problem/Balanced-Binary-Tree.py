# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def height(self, root:Optional[TreeNode]) ->int:
        if not root:
            return 0
        l_h = self.height(root.left)
        if l_h == -1:
            return -1
        r_h = self.height(root.right)
        if r_h == -1:
            return -1
        if abs(l_h-r_h)>1:
            return -1
        return 1 + max(l_h,r_h)
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Unbalanced if max_depth of left subtree and right subtree differs more than by 1
        return self.height(root) != -1
            

        