class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        presence = {}
        for i  in range(len(nums)):
            x = presence.get(nums[i])
            if x != None and abs(x-i) <= k:
                return True
            else:
                presence[nums[i]] = i
        return False

        