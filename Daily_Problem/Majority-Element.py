class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        count = {} #Space Complexity: O(n)
        con=len(nums)//2
        for i in nums: #Time Complexity: O(n)
            if i in count:
                count[i] +=1
                if count[i]>con:
                    return i
            else:
                count[i]=1

        ### How to solve the problem in linear time and in O(1) space ?
        
        
        