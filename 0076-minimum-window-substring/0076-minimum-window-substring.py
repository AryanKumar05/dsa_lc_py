from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        best=float('inf')
        freq_of_t={}
        for i in range(len(t)):
            freq_of_t[t[i]]=freq_of_t.get(t[i],0)+1
        def matches(window,freq_of_t):
            for char in freq_of_t.keys():
                if window.get(char, 0) < freq_of_t[char]:
                    return False
            return True
            
        
        window={}
        left=0
        for right in range(len(s)):
            window[s[right]]=window.get(s[right],0)+1
            while matches(window,freq_of_t):
                if right-left+1<best:
                    best=right-left+1
                    result=s[left:right+1]
                
                window[s[left]]-=1
                if window[s[left]]==0:
                    del window[s[left]]
                left+=1

        return result if best!=float('inf') else ""
        
