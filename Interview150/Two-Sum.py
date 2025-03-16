# With the Idea of Hash Table
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_={}
        dict_[(target-nums[0])]=0
        for i in range(1,len(nums)):
            if nums[i] in dict_:
                return [dict_[nums[i]], i]
            dict_[(target-nums[i])]=i
        
            