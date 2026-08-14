from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        k=len(p)
        freq={}
        result=[]
        if len(s) < len(p):
            return []
        for i in range(k):
            freq[s[i]]=freq.get(s[i],0)+1
        if freq==Counter(p):
            result.append(0)
        for i in range(k,len(s)):
            freq[s[i]]=freq.get(s[i],0)+1
            freq[s[i-k]]-=1
            if freq[s[i-k]]==0:
                del freq[s[i-k]]
            if freq==Counter(p):
                result.append(i-k+1)
        return result
        


            
        


            

        