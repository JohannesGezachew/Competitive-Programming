class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        count = 0
        n = len(nums)

        for i in range(n):
            start = bisect_left(nums, lower - nums[i], i + 1, n)
            end = bisect_right(nums, upper - nums[i], i + 1, n) - 1

            if start <= end:
                count += (end - start + 1)

        return count