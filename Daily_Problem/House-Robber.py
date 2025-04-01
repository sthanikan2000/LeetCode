class Solution:
    def rob(self, nums: List[int]) -> int:
        n =len(nums)
        if n<=1:
            return nums[0]

        dp = [0]*n
        dp[n-1] = nums[n-1]
        dp[n-2] = max(nums[n-2],nums[n-1])
        for i in range(n-3,-1,-1):
            dp[i] = max(dp[i+1],nums[i]+dp[i+2])
        return dp[0]

        '''
        ### Simple brute force solution
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        return max(self.rob(nums[1:]),nums[0]+self.rob(nums[2:]))
        '''

        