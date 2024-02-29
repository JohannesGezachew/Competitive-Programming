class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        
        k = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[r - 1]:
                nums[k] = nums[r]
                k += 1
        
        return k
        
        