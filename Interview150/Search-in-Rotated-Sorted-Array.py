class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def find_0_ind_asc(nums):
            # In not rotated return -1
            n = len(nums)
            if n==1: # 1 <= nums.length <= 5000
                return -1
            l = 0 
            r = n-2
            while l<=r:
                m = (l+r)//2
                if nums[m]>nums[m+1]:
                    return m+1
                if nums[l]<=nums[m]:
                    l=m+1
                else:
                    r=m-1
            return -1
        
        n = len(nums)
        p = find_0_ind_asc(nums)
        # print(p)
        if p == -1:
            p = n
        l = 0
        r = n-1
        while l<=r:
            m = (l+r)//2
            m_ = (p+m)%n
            # print(m,m_)
            if nums[m_] == target:
                return m_
            elif nums[m_] < target:
                l = m+1
            else:
                r = m-1
        return -1
        