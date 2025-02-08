class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k=0
        for i in nums:
            if val==i:
                continue
            else:
                nums[k]=i
                k+=1
        return k
