def counter(i):
    count=0
    while i:
        i&=i-1
        count+=1
    return count   
    
class Solution(object):
        
        
    def countBits(self, n):
            
        idx=[]
        for i in range(n+1):
            bits=counter(i)
            idx.append(bits)
        
        return idx

           