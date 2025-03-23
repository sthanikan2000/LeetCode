class Solution:
    def maxArea(self, height: List[int]) -> int:
        s = 0
        e = len(height)-1
        max_v = 0
        while s<e:
            if height[s]<=height[e]:
                v = (e-s)*height[s]
                s+=1
            else:
                v = (e-s)*height[e]
                e-=1
            if v > max_v:
                max_v = v
        return max_v
            

            
        