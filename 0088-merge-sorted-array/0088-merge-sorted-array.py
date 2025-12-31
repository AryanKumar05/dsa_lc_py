class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i=0
        j=0
        
        while i<m+n and j<n:
            ptr_a=nums1[i]
            ptr_b=nums2[j]
            if nums1[i]==0:
                nums1[i]=ptr_b
                j+=1
            i+=1
        nums1.sort()
        return nums1


        """
        Do not return anything, modify nums1 in-place instead.
        """
        