class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        x = 0
        y = []
        for i in nums:
            if i ==1:
                x += 1
            elif i != 1:
                y.append(x)
                x = 0
        y.append(x)
        return(max(y))
