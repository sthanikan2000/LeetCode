class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
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

            
            

        