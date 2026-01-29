class Solution(object):
    def thirdMax(self, nums):
        max=sorted(set(nums))
        if len(max)<3:
            return max[-1]
        return max[-3]

       
        