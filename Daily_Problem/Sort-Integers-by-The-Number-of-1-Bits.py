class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def one_bits(x:int) -> int:
            c = 0 
            while x>0:
                c += (x&1)
                x >>= 1
            return c
        arr.sort(key=lambda x:(one_bits(x),x))
        return arr
        