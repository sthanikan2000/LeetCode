class Solution:
    def hIndex(self, citations: List[int]) -> int:
        '''
        ### Method 1
        citations.sort(reverse=True)
        len_c =len(citations)
        i = 0 
        while i<len_c:
            if citations[i] < i+1:
                break
            i+=1
        return i
        '''
        citations.sort()
        if citations[-1] == 0:
            return 0
        len_c = len(citations)
        for i,c in enumerate(citations):
            if c >= len_c-i:
                return len_c-i
