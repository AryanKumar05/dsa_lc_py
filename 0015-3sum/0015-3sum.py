class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result=[]
        n=len(nums)
        for i in range(n-2):
            # skip duplicates for fixed
            if i>0 and nums[i]==nums[i-1]:   
                continue
            left=i+1
            right=n-1
            
            while left<right:
                sum=nums[i]+nums[left]+nums[right]
                if sum<0:
                    left+=1
                    
                elif sum>0:
                    right-=1
                else:
                    result.append([nums[i],nums[left],nums[right]])
                    # remove duplicates
                    while left<right and nums[left]==nums[left+1]:
                        left+=1
                    while left<right and nums[right]==nums[right-1]:
                        right-=1


                   # check for more    
                    left+=1
                    right-=1
                    

        return result
                



        
        