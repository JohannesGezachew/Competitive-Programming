class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        msum = 0
        res = float("inf")
        for right in range(len(nums)):
            msum += nums[right]
            while msum >= target:
                res = min(res, right - left + 1)
                msum -= nums[left]
                left += 1
            # right += 1
        return 0 if res == float("inf") else res


                
