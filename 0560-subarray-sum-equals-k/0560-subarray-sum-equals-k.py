class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        curr_sum = 0
        counter = Counter([0])
        count  = 0
        for right in range(len(nums)):
            curr_sum += nums[right]
            if curr_sum - k in counter:
                count += counter[curr_sum - k]
            counter[curr_sum] += 1
        return count
