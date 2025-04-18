# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        q = [root]
        pop_left = True
        while q:
            len_q = len(q)
            res.append([])
            if pop_left:
                for _ in range(len_q):
                    node = q.pop(0)
                    res[-1].append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                pop_left = False
            else:
                for _ in range(len_q):
                    node = q.pop()
                    res[-1].append(node.val)
                    if node.right:
                        q.insert(0,node.right)
                    if node.left:
                        q.insert(0,node.left)
                pop_left = True
        return res
            
            
        