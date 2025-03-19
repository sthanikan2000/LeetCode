class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ### ---------- Normal Addition and Subtraction ----------------------------
        x = 0
        for i in range(len(nums)):
             x += i+1
             x -= nums[i]
        return x

        '''
        ####  --------- Bit Manupulation ------------------
        x = 0
        for i in range(len(nums)):
            x ^= i+1
            x ^= nums[i]
        return x
        '''
        