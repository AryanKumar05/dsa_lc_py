class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d={}
        for i ,num in enumerate(nums):
            if num in d and abs(i-d[num])<=k:
                return True
            else:
                d[num]=i
        return False


        