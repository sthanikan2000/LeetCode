class Solution:
    def rob(self, nums: List[int]) -> int:
        ### Best Solution with time complexity: O(n)
        n =len(nums)
        if n<=1:
            return nums[0]
        max_rob_from = [0]*n
        max_rob_from[n-1] = nums[n-1]
        max_rob_from[n-2] = max(nums[n-2],nums[n-1])
        for i in range(n-3,-1,-1):
            max_rob_from[i] = max(max_rob_from[i+1],nums[i]+max_rob_from[i+2])
        return max_rob_from[0]

        '''
        ### Simple brute force solution
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        return max(self.rob(nums[1:]),nums[0]+self.rob(nums[2:]))
        '''

        