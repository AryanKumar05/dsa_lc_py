class Solution:
    def isPalindrome(self, s: str) -> bool:
        result=""
        for char in s:
            if char.isalnum():
                result+="".join(char)

        
        
        if result.lower()==result[::-1].lower():
            return True
        else:
            return False
        