class Solution:
    def maxArea(self, height: List[int]) -> int:
        n=len(height)
        i=0
        j=n-1
        max_area=0
        while i<j:
            current_area=min(height[i],height[j])*(j-i)
            if max_area<current_area:
                max_area=current_area
            if height[i]<=height[j]:
                i+=1
            else:
                j-=1
        return max_area
