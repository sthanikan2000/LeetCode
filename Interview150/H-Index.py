class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        len_c =len(citations)
        i = 0 
        while i<len_c:
            if citations[i] < i+1:
                break
            i+=1
        return i