class Solution(object):
    def lengthOfLastWord(self, s):
        s=s.strip(' ')
        str=s.split(" ")
        return (len(str[-1]))
        """
        :type s: str
        :rtype: int
        """
        