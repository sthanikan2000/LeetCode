# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        d = 0 
        q = [root]
        while q:
            temp_lst = []
            for node in q:
                if not node.left and not node.right:
                    return d+1
                if node.left:
                    temp_lst.append(node.left)
                if node.right:
                    temp_lst.append(node.right)
            q = temp_lst
            d+=1
                

        '''
        ### Recursion Approach but not Optimal
        if not root:
            return 0
        # if not root.left and not root.right:
        #     return 1
        if not root.left:
            return 1 + self.minDepth(root.right)
        if not root.right:
            return 1 + self.minDepth(root.left)
        return 1 + min(self.minDepth(root.right),self.minDepth(root.left))
        '''
        