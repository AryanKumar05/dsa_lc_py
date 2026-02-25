class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d={}
        seen=set()
        if len(s)==len(t):
            for i,char in enumerate(s):
                if char not in d.keys():

                    if t[i] in seen:
                        return False
                    d[char]=t[i]
                    seen.add(t[i])
                else:
                    if d[char]!=t[i]:
                        return False

        else:
            return False
        return True
        