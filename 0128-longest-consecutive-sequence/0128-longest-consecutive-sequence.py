class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        ans = 1
        right =[]
        if len(nums) > 0: 
            nums= list(set(nums))
            nums.sort()
            for i in range(len(nums)-1):
                if nums[i] + 1 == nums[i+1]:
                    ans += 1
                if nums[i] + 1 != nums[i+1]:
                    right.append(ans)
                    ans = 1
            right.append(ans)
            
            return(max(right))
        else:
            return 0
