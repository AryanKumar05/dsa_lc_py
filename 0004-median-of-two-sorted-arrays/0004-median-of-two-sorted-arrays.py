class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        m=len(nums1)
        n=len(nums2)
        left=0
        right=m
        half=(m+n+1)//2
        while left<=right:
            mid1=left+(right-left)//2
            mid2=half-mid1
            max_left1=float('-inf') if mid1==0 else nums1[mid1-1]
            min_right1=float('inf') if mid1==m else nums1[mid1]
            max_left2=float('-inf') if mid2==0 else nums2[mid2-1]
            min_right2=float('inf') if mid2==n else nums2[mid2]
            #update to find partitions

            if max_left1<=min_right2 and max_left2<=min_right1:
                if (m+n)%2==1:
                    return max(max_left1,max_left2)
                else:
                    return  (max(max_left1,max_left2)+ min(min_right1,min_right2))/2.0
            elif max_left1>min_right2:
                right=mid1-1
            else:
                left=mid1+1
        return 0.0






        