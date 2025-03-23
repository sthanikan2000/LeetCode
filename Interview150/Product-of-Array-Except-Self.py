class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0]*n
        res[1] = nums[0]
        for i in range(2,n):
            res[i] = res[i-1] * nums[i-1]
        x = nums[n-1]
        # print(res)
        for i in range(n-2,0,-1):
            # print(i,x)
            res[i] *= x
            x *= nums[i]
        res[0] = x
        return res
        '''
        ### Not memory Efficient
        n = len(nums)
        pro_1 = [0]*(n-1)
        pro_2 = [0]*(n-1)
        pro_1[0] = nums[0]
        pro_2[n-2] = nums[n-1]

        for i in range(n-2):
            pro_1[i+1] = pro_1[i]*nums[i+1]
            pro_2[n-3-i] = pro_2[n-2-i]*nums[n-2-i]

        res = [0]*n
        res[0] = pro_2[0]
        res[n-1] = pro_1[n-2]
        for i in range(n-2):
            res[i+1] = pro_1[i]*pro_2[i+1]
        return res
        '''

        