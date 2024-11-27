class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0
        right = k
        current_sum = sum(nums[0:k])
        while right < len(nums):
            current_sum = max(current_sum, (current_sum - nums[left] + nums[right]))
            left += 1
            right += 1
        return current_sum/k
