# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []
        queue = [root]
        total = 0
        while queue:
            temp = []
            for node in queue:
                total += node.val
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            res.append(total/len(queue))
            total = 0
            queue = temp
        return res