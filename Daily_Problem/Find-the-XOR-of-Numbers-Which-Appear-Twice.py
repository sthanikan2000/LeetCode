class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        x=0
        hash_map={}
        for num in nums:
            if num in hash_map:
                x = x ^ num
            else:
                hash_map[num]=""
        return x

        