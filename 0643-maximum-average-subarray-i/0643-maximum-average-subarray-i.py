class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])
        n = len(nums)
        max_sum = window_sum
        for i in range(n-k):
            window_sum = window_sum - nums[i] + nums[i+k]
            max_sum = max(window_sum, max_sum)
        return max_sum /k