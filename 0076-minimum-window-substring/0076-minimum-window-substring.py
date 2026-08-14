# from collections import Counter
# class Solution:
#     def minWindow(self, s: str, t: str) -> str:
#         best=float('inf')
#         freq_of_t={}
#         for i in range(len(t)):
#             freq_of_t[t[i]]=freq_of_t.get(t[i],0)+1
#         def matches(window,freq_of_t):
#             for char in freq_of_t.keys():
#                 if window.get(char, 0) < freq_of_t[char]:
#                     return False
#             return True
            
        
#         window={}
#         left=0
#         for right in range(len(s)):
#             window[s[right]]=window.get(s[right],0)+1
#             while matches(window,freq_of_t):
#                 if right-left+1<best:
#                     best=right-left+1
#                     result=s[left:right+1]
                
#                 window[s[left]]-=1
#                 if window[s[left]]==0:
#                     del window[s[left]]
#                 left+=1

#         return result if best!=float('inf') else ""
        
# ----------------------Method one O(n*m) because each right expansion matches check again and again----------------------
class Solution:

    def minWindow(self, s: str, t: str) -> str:
        best = float("inf")
        result = ""

        freq_of_t = {}
        for char in t:
            freq_of_t[char] = freq_of_t.get(char, 0) + 1

        # Instead of calling matches(), track how many unique chars are fully satisfied
        have = 0
        need = len(freq_of_t)

        window = {}
        left = 0
        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char, 0) + 1

            # IF this addition made s[right] reach its required frequency in t:
            if char in freq_of_t and window[char] == freq_of_t[char]:
                have += 1

            # 'have == need' replaces 'matches(window, freq_of_t)' instantly!
            while have == need:
                if right - left + 1 < best:
                    best = right - left + 1
                    result = s[left : right + 1]

                # Before removing s[left], check if it breaks a satisfied requirement
                left_char = s[left]
                if (
                    left_char in freq_of_t
                    and window[left_char] == freq_of_t[left_char]
                ):
                    have -= 1

                window[left_char] -= 1
                if window[left_char] == 0:
                    del window[left_char]

                left += 1

        return result if best != float("inf") else ""