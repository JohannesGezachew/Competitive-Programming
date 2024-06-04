class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        holder = 0
        ans =0
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                holder +=1
            ans +=holder
        return ans
        
