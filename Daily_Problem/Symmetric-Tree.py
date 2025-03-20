# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        '''
        ### Exact Depth First search - NOT a Optimal Solution, But Passed all test Cases
        if (not root):
            return True
        s1=[root.left]
        s2=[root.right]
        while s1 and s2:
            x=s1.pop(-1)
            y=s2.pop(-1)
            if (x and y):
                # print(x.val,y.val)
                if x.val != y.val:

                    return False
                s1.append(x.right)
                s1.append(x.left)
                s2.append(y.left)
                s2.append(y.right)
            elif not x and not y:
                continue
            else:
                return False
        return True
        '''

        
        ### Exact Breath First Search - Optimal Solution
        if (not root):
            return True
        q1=[[root.left]]
        q2=[[root.right]]
        while q1 and q2:
            x = q1.pop(0)
            y = q2.pop(0)
            x1=[]
            y1=[]
            for i in range(len(x)):
                if (x[i] and y[i]):
                    if x[i].val != y[i].val:
                        return False
                   
                    x1.append(x[i].left)
                    y1.append(y[i].right)
                
                    x1.append(x[i].right)
                    y1.append(y[i].left)
                    
                elif not x[i] and not y[i]:
                    continue
                else:
                    return False
            if not x1:
                break
            q1.append(x1)
            q2.append(y1)
        return True
        