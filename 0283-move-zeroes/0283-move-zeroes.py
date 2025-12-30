class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zeros=nums.count(0)
        nums[:]=[x for x in nums if x!=0]
        
        nums.extend([0]*zeros)

        """
        

        Do not return anything, modify nums in-place instead.
        """
        