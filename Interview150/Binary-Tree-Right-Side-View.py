# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res  = []
        queue = [root]
        while queue:
            res.append(queue[0].val)
            temp = []
            for node in queue:
                if node.right:
                    temp.append(node.right)
                if node.left:
                    temp.append(node.left)
            queue = temp
        return res
        