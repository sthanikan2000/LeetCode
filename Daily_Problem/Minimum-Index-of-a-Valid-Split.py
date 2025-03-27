class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        counts = {}
        dom_fre = 0
        dom_ele = None
        for i in nums:
            x = counts.get(i,0)
            if x+1>dom_fre:
                dom_ele=i
                dom_fre=x+1
            counts[i] = x+1
        c = 0
        n = len(nums)
        for i in range(n):
            if nums[i] == dom_ele:
                c+=1
                if c>(i+1)//2 and dom_fre-c>(n-1-i)//2:
                    return i
        return -1
            

        