class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        i=1
        while i<=len(strs[0])   : 
            
            prefix=strs[0][:i]
            for word in strs:
                if not word.startswith(prefix) :
                    return strs[0][:i-1]
            i+=1
        return strs[0]

            

        