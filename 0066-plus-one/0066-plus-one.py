class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] != 9:
            Increm_num = digits.pop(-1)+1 
            digits.append(Increm_num)
            return(digits)
        else:
            Increm_num = ''.join(map(str,digits))
            digits.clear()
            Increm_num = str(int(Increm_num) +1)
            print(Increm_num)
            for i in range(len(Increm_num)):
                digits.append(int(Increm_num[i]))
            return digits
