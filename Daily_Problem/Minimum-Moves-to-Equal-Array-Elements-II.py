class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        if n%2 == 0:
            mid = n//2
            x = (nums[mid-1]+nums[mid])//2
        else:
            x = nums[n//2]
        res = 0
        for i in nums:
            res += abs(i-x)
        return res