class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        minprefixsum = 0
        csum = 0

        for num in nums:
            csum += num
            minprefixsum = min(csum, minprefixsum)
        
        return 1 - minprefixsum