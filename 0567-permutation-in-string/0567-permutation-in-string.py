from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        k=len(s1)
        freq={}
        
        if len(s2) < len(s1):
            return False
        for i in range(k):
            freq[s2[i]]=freq.get(s2[i],0)+1
        if freq==Counter(s1):
            return True
        for i in range(k,len(s2)):
            freq[s2[i]]=freq.get(s2[i],0)+1
            freq[s2[i-k]]-=1
            if freq[s2[i-k]]==0:
                del freq[s2[i-k]]
            if freq==Counter(s1):
                return True
        return False
        