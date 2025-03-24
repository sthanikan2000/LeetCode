class Solution:
    def hIndex(self, citations: List[int]) -> int:
        '''
        ### Method 1 - Reverse sort & linear search
        citations.sort(reverse=True)
        len_c =len(citations)
        i = 0 
        while i<len_c:
            if citations[i] < i+1:
                break
            i+=1
        return i
        '''
        '''
        ### Method 2 - Sorting & Linear Search
        citations.sort()
        if citations[-1] == 0:
            return 0
        len_c = len(citations)
        for i,c in enumerate(citations):
            if c >= len_c-i:
                return len_c-i
        '''
        ### Method 3 - Sorting & Binary search
        citations.sort(reverse = True)
        l = 0
        r = len(citations) - 1
        h_i = 0
        while l<=r:
            mid = (l+r)//2
            if citations[mid]>= mid+1:
                h_i = mid+1
                l= mid+1
            else:
                r = mid-1
        return h_i