class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ""
        while columnNumber > 0:
            remainder = columnNumber % 26
            if remainder == 0:
                remainder = 26
                columnNumber -= 1
            result += chr(remainder + 64)  
            columnNumber //= 26
        return result[::-1]