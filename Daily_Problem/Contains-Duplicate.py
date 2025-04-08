class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        presence = {}
        for num in nums:
            if presence.get(num) != None:
                return True
            presence[num] = True
        return False
        