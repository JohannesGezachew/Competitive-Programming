class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return 0

        negative = num < 0
        num_str = str(abs(num))
        digits = list(num_str)

        zeros = [digit for digit in digits if digit == '0']
        non_zeros = [digit for digit in digits if digit != '0']
        
        if negative:

            non_zeros.sort(reverse=True)
            result = "-" + "".join(non_zeros) + "".join(zeros)
        else:

            non_zeros.sort()

            result = non_zeros[0] + "".join(zeros) + "".join(non_zeros[1:])
        
        return int(result)


