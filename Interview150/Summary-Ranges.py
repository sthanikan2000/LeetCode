class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        elif len(nums)==1:
            return [f\{nums[0]}\]
        res = []
        n = len(nums)
        f = 0
        for i in range(1,n):
            if nums[i] != nums[i-1] + 1 and f == i - 1:
                res.append(f\{nums[f]}\)
                f = i 
            elif nums[i] != nums[i-1] + 1 and f != i-1:
                res.append(f\{nums[f]}->{nums[i-1]}\)
                f = i
            if nums[i] == nums[i-1] + 1 and i == n-1:
                res.append(f\{nums[f]}->{nums[i]}\)
            elif i == n-1:
                res.append(f\{nums[f]}\)       
        return res