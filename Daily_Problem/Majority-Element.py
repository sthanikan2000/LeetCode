class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        '''
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
        '''
        ### How to solve the problem in linear time and in O(1) space ?

        # Since it is gurantee that majority element appears more than floor(n/2)
        # we can pair the majority element with other elements
        # and then their will atleast one majority elements needs a pair
        majority = 0
        majority_ele = None
        for num in nums:
            if majority == 0:
                majority +=1
                majority_ele=num
                continue
            if num != majority_ele:
                majority -= 1
            else:
                majority += 1
        return majority_ele
            
        
        
        