# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        ### If InOrderTraversal return ascending order, then tree is valid BST
        prev = [float(\-inf\)]
        def ascendingInOrder(root: Optional[TreeNode], lst)->bool:
            if not root:
                return True
            if root.left:
                if not ascendingInOrder(root.left,lst):
                    return False
            if lst[0]>=root.val:
                return False
            lst[0] = root.val
            if root.right:
                if not ascendingInOrder(root.right,lst):
                    return False
            return True
        return ascendingInOrder(root,prev)
        

        