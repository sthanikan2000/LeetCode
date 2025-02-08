class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {nums[0]:1}
        majority = nums[0]

        for i in nums[1:]:
            if i in count:
                count[i]+=1
                if count[i]>count[majority]:
                    if count[i]> len(nums)//2:
                        return i
                    majority = i
            else:
                count[i]=1
        return majority
            
        
        
        