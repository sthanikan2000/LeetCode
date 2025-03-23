class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        len_n=len(nums)
        res = []
        for i in range(len_n-2):
            if i>0 and nums[i] == nums[i-1]:
                continue

            s = i+1
            e = len_n-1

            while s<e:
                x = nums[i]+nums[s]+nums[e] 

                if x == 0:
                    res.append([nums[i],nums[s],nums[e]])
                    s+=1
                    
                    while nums[s] == nums[s-1] and s<e:
                        s+=1

                elif x < 0:
                    s+=1
                else:
                    e-=1     
        return res
        