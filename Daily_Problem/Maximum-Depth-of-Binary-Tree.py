# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        ### Breath First Search
        if (not root):
            return 0
        q=[root]
        d=0
        while q:
            len_q = len(q)
            for i in range(len_q):
                x = q.pop(0)
                if x.left:
                    q.append(x.left)
                if x.right:
                    q.append(x.right)
            d+=1
        return d

        