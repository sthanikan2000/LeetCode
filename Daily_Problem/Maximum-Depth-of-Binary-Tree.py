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
        d=1
        while q:
            next_q=[]
            for i in range(len(q)):
                if q[i].left:
                    next_q.append(q[i].left)
                if q[i].right:
                    next_q.append(q[i].right)
            if next_q:
                d+=1
            q = next_q
        return d

        