# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        ### Beats 100% time complexity
        if not root:
            return 0
        q = [(root,1)]
        while q:
            x,d = q.pop(0)
            if not x.left and not x.right:
                return d
            if x.left:
                q.append((x.left,d+1))
            if x.right:
                q.append((x.right,d+1))
        '''
        ### Only beat 82% time complexity
        if not root:
            return 0
        d = 1 
        q = [root]
        while q:
            len_q = len(q)
            for _ in range(len_q):
                x = q.pop(0)
                if not x.left and not x.right:
                    return d
                if x.left:
                    q.append(x.left)
                if x.right:
                    q.append(x.right)
            d+=1
        '''      

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
        