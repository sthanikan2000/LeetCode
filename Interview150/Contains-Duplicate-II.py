class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        presence = {}
        for i  in range(len(nums)):
            if i > k:
                del presence[nums[i-k-1]]
            if presence.get(nums[i]):
                return True
            else:
                presence[nums[i]] = True
        return False

        