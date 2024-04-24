class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        left = 0
        right = 1

        while right < len(nums):
            if nums[left] == nums[right]:
                nums[left] = nums[left] * 2
                nums[right] = 0
            left += 1
            right += 1
        non_zero = [x for x in nums if x != 0]
        zeros = [0] * (len(nums) - len(non_zero))
        return non_zero + zeros