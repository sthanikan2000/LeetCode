# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        g_sto = {\prev\:None,\min_diff\:float(\inf\)}
        def InOrder(root,storage):
            if root:
                InOrder(root.left,storage)
                if storage[\prev\] == None:
                    storage[\prev\] = root.val
                else:
                    diff = abs(storage[\prev\]-root.val)
                    if diff<storage[\min_diff\]:
                        storage[\min_diff\] = diff
                    storage[\prev\] = root.val
                InOrder(root.right,storage)
        InOrder(root,g_sto)
        return g_sto[\min_diff\]


        