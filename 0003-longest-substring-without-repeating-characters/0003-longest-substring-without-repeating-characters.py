class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window={}
        left=0
        best=0
        for right in range(len(s)):
            window[s[right]]=window.get(s[right],0)+1
            while window[s[right]] >1:
                window[s[left]]-=1
                if window[s[left]]==0:
                    del window[s[left]]
                left+=1
            best=max(best,right-left+1)
        return best