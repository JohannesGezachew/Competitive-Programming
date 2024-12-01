class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        forward = [0 , 1]
        backward = [0, 1]
        count = []

        for i in range(1, len(nums)):
            forward.append(forward[-1] + 1 if nums[i] <= nums[i - 1] else 1)
        
        for j in range(len(nums) - 2, -1, -1):
            backward.append(backward[-1] + 1 if nums[j] <= nums[j + 1] else 1)

        backward.reverse()
        for right in range(1, len(forward)):
            if forward[right - 1] >= k and backward[right] >= k:
                count.append(right - 1)
        
        return count
