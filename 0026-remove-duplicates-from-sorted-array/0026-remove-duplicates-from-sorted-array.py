class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        right = 0
        count = 1
        if not nums:
            return 0


        while right < len(nums):
            if nums[left] == nums[right]:
                right += 1
            else:
                count += 1
                nums[left + 1] = nums[right]
                left += 1
                
        return count