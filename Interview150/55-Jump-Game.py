class Solution:
    def canJump(self, nums: List[int]) -> bool:
        can_jump  = nums[0]
        for i in nums[1:]:
            can_jump -= 1
            if can_jump < 0:
                return False
            elif can_jump<i:
                can_jump = i
        return True
        