class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=1
        for i in nums[1:]:
            if nums[k-1]==i:
                continue
            else:
                nums[k]=i
                k+=1
        return k
        