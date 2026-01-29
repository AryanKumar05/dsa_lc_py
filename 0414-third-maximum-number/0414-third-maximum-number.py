class Solution(object):
    def thirdMax(self, nums):
        shash=set(nums)
        num=list(shash)
        print(num)
        num=sorted(num)
        if len(num)<3:
            return num[-1]
        return num[-3]

        """
        :type nums: List[int]
        :rtype: int
        """
        