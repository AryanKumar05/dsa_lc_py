class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num=""
        final_list=[]
       
        num=''.join(str(digit) for digit in digits)
        print(num)
        number=int(num)
        final=str(number+1)
        for digit in final:
            final_list.append(int(digit))
        return final_list

        