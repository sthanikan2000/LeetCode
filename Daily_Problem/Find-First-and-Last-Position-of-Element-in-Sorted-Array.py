class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        s=0
        e=len(nums)-1
        ind=None
        while s<=e:
            mid = (s+e)//2
            if nums[mid]==target:
                ind=mid
                break
            if nums[mid]<target:
                s=mid+1
            else:
                e=mid-1
        if ind == None:
            return [-1, -1]

        f_i=ind
        e1=ind 
        while s<=e1: # Here s is the result after first while loop used for the finding a index
            mid = (s+e1)//2
            if nums[mid]==target:
                e1=mid-1
                f_i=mid
            else:
                s=mid+1
        
        e_i=ind
        s1=ind
        while s1<=e: # Here e is the result after first while loop used for the finding a index
            mid = (s1+e)//2
            if nums[mid]==target:
                s1=mid+1
                e_i=mid
            else:
                e = mid-1
        return [f_i,e_i]            
        