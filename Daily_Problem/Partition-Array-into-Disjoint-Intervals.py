class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        n = len(nums)
        max_l = nums[0]
        c_max = max_l # current maximum
        p_i = 0 # current partition index - 1
        for i in range(1,n):
            if nums[i]<max_l:
                p_i = i
                max_l = c_max
            elif nums[i]>c_max:
                c_max = nums[i]
        return p_i+1
        '''
        ### Complex solution beats 98% runtime
        max_l = nums[0]
        n = len(nums)
        i =1
        x =1
        while i<n:
            if max_l <= nums[i]:
                y = i+1
                while y<n:
                    if nums[y]>=max_l:
                        y+=1
                        continue
                    break
                else:
                    return i
                max_l=nums[i]
                i+=1
                continue
            else:
                i+=1
                x = i
        return x
        '''

            
            

        