class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # zeros=nums.count(0)
        # nums[:]=[x for x in nums if x!=0]
        
        # nums.extend([0]*zeros)
        insert=0
        for i in range(0,len(nums)):
            if nums[i]!=0:
                nums[insert],nums[i]=nums[i],nums[insert]
                insert+=1

        """
        

        

        Do not return anything, modify nums in-place instead.
        """
        