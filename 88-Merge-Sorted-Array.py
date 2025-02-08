class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        \\\
        Do not return anything, modify nums1 in-place instead.
        \\\
        i=j=0
        last_next_nums1=m
        while j<n and i<m+n:
            if i >= last_next_nums1:
                nums1.insert(i,nums2[j])
                nums1.pop(-1)
                i+=1
                j+=1
            elif nums1[i]<nums2[j]:
                i += 1
            else:
                nums1.insert(i,nums2[j])
                nums1.pop(-1)
                i+=1
                j+=1
                last_next_nums1 += 1