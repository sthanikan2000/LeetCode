class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)<3:
            return len(nums)

        k=2
        for i in nums[2:]:
            if i == nums[k-1] and  i == nums[k-2]:
                    continue
            else:
                nums[k]=i
                k+=1
        return k
        