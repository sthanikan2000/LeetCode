class Solution:
    def hIndex(self, citations: List[int]) -> int:
        ### iterate from front
        res = 0
        n = len(citations)
        l = 0
        r = n -1
        while l<=r:
            # print(l,r)
            mid = (l+r)//2
            if citations[mid] >= n-mid:
                res = n-mid
                r = mid-1
            else:
                l = mid+1
        return res
        