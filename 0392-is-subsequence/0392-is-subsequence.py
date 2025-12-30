class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        prev = -1
        for char in s:
            pos = t.find(char, prev + 1)
            if pos == -1:
                return False
            prev = pos
        return True
