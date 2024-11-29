class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0
        right = k
        csum = sum(nums[:k])
        msum = csum
        
        if right == len(nums):
            return csum / k
        
        while right < len(nums):
            csum = csum + nums[right] - nums[left]
            msum = max(msum, csum)  
            left += 1
            right += 1
        
        return msum / k