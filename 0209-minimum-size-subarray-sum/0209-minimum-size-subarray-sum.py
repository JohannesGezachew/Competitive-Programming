class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float("inf")
        left = 0
        right = 0
        min_sum = 0
        for right in range(len(nums)):
            min_sum += nums[right]

            while min_sum >= target:
                res = min(res, right- left +1)
                min_sum =min_sum - nums[left]
                left += 1
                
        return 0 if res == float("inf")  else res