class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # since condition is more than floor(n/3)
        # there can be either one or two elements, not more than that
        if len(nums) == 1:
            return nums
        counts = {nums[0]:1}

        f_m = nums[0]
        s_m = None

        for num in nums[1:]:
            counts[num] = counts.get(num,0) + 1
            if num == f_m:
                continue
            if s_m != None and num == s_m:
                if counts[f_m]<counts[s_m]:
                    s_m = f_m
                    f_m = num
                continue
            if s_m == None:
                s_m = num
                continue
            if counts[num] >= counts[f_m]:
                s_m = f_m
                f_m = num
            elif counts[num] >= counts[s_m]:
                s_m = num
            # elif s_m == None:
            #     s_m = num

        con = len(nums)//3

        x=[]
        if counts[f_m]>con:
            x.append(f_m)
        if s_m and counts[s_m]>con:
            x.append(s_m)
        return x

        '''
        #### This code fails for some test cases
        f_m=[nums[0],1]
        s_m=[None,0]
        for i in nums[1:]:
            if i == f_m[0]:
                f_m[1]+=1
                continue
            
            if s_m[0] == i:
                s_m[1]+=1
                continue
            
            if s_m[0] == None:
                s_m = [i,1]
                continue

            s_m[1] -= 1
            if s_m[1] == 0:
                s_m = [i,1]

            f_m[1] -= 1
            if f_m[1] == 0:
                f_m = s_m
                s_m = [None,0]

        x=[]
        if len(nums)<=3:
            x.append(f_m[0])
            if s_m[0]:
                x.append(s_m[0])
            return x
            
        
        if f_m[1] > 0:
            x.append(f_m[0])
        if s_m[1] > 1:
            x.append(s_m[0])
        return x
        '''