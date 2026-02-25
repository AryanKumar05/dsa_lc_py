class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]

        dict={'(':')','{':'}','[':']'}
        for char in s:
            if char in dict.keys():
                stack.append(char)
            else:
               if stack==[] or  char!=dict[stack.pop()] :
                return False
        return True if stack==[] else False

        