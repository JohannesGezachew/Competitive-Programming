class Solution:
    def largestOddNumber(self, num: str) -> str:
        odd = []
        if int(num) % 2 == 0:
            for i in num:
                if not int(i) % 2 ==0:
                    odd.append(i)
            if odd == []:
                return ""
            else:
                return(max(odd))
        else:
            return num