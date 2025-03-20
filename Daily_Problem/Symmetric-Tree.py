# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if (not root):
            return True
        q1=[root.left]
        q2=[root.right]
        while q1 and q2:
            x = q1.pop(0)
            y = q2.pop(0)
            if (x and y):
                if x.val != y.val:
                    return False
                q1.append(x.right)
                q1.append(x.left)
                q2.append(y.left)
                q2.append(y.right)
            elif not x and not y:
                continue
            else:
                return False
        return True

            


        
        