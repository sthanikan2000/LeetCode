class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def custom_sort_key(x):
            x0 = x
            c = 0 
            while x>0:
                c += (x&1)
                x >>= 1
            return (c,x0)
        arr.sort(key=custom_sort_key)
        return arr
        