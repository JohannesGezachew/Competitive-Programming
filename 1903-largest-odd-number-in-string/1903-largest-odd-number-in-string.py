class Solution:
    def largestOddNumber(self, num: str) -> str:
        right = len(num) - 1
        while right >= 0 and int(num[right]) % 2 == 0:
            right -= 1
        
        if right == -1:
            return ""
        else:
            return num[:right+1]
