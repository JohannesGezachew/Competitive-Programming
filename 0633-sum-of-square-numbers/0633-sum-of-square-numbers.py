class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left = 1
        right = floor(sqrt(c))
        while left <= right :
            x = (left**2)+(right**2)
            if  x== c:
                return True
            elif x >c:
                left +=1
            elif x< c:
                right +=1
            
        return False