class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        max_ele = nums[0]
        max_diff = nums[0]-nums[1]
        max_val = max_diff*nums[2]
        for i in range(3,n):
            max_ele = max(max_ele,nums[i-2])
            max_diff = max(max_diff,max_ele-nums[i-1])
            max_val = max(max_val,max_diff*nums[i])
        if max_val<0:
            return 0
        return max_val

        