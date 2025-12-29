class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x)==str(x)[::-1]
        print(str(x)[::-1])
        # temp1=0
        # temp2=x
        # while(x !=0):
        #     temp1=temp1*10+x%10
        #     x=x/10
        # if (temp1==temp2):
        #     True
        # else:
        #     False
        


        