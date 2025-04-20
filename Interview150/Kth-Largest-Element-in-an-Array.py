from heapq import heapify,heappop
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        heapify(nums)
        for _ in range(n-k):
            heappop(nums)
        return heappop(nums)


        