class Solution:
    def reverseWords(self, s: str) -> str:
        rev=""
        wordlist=s.split()
        reverselist=wordlist[::-1]
        
        for word in reverselist:
            rev+=word+" "
        return rev.strip()

        