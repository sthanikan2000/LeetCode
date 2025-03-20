# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        list_ = []
        if not root:
            return list_
        list_ += self.inorderTraversal(root.left)
        list_.append(root.val)
        list_ += self.inorderTraversal(root.right)
        return list_