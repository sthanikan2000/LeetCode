class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        '''
        ### Usage of prefix maximum and suffix maximum
        n= len(nums)
        prefix_max = [nums[0]]
        suffix_max = [nums[n-1]]
        for i in range(1,n):
            prefix_max.append(max(nums[i],prefix_max[-1]))
            suffix_max.insert(0,max(nums[n-1-i],suffix_max[0]))
        max_val = 0
        for i in range(1,n-1):
            max_val = max(max_val,(prefix_max[i-1]-nums[i])*suffix_max[i+1])
        return max_val

        '''
        n = len(nums)
        max_ele = 0
        max_diff = 0
        max_val = 0
        for i in range(2,n):
            max_ele = max(max_ele,nums[i-2])
            max_diff = max(max_diff,max_ele-nums[i-1])
            max_val = max(max_val,max_diff*nums[i])
        return max_val
    

        