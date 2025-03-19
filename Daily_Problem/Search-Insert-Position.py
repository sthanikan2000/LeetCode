class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        s = 0
        e = len(nums) - 1
        # found=False
        while s<=e:
            mid = (s+e)//2
            if nums[mid]==target:
                return mid
            if nums[mid]<target:
                s = mid+1
            else:
                e = mid-1
        return s