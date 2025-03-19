class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        x=0
        for i in nums:
            if i<k:
                x+=1
        return x
        